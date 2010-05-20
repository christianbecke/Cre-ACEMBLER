# vim: encoding=utf-8 ts=4 sw=4 noexpandtab :

# CreRecEMBL - in silico loxP/Cre recombination
# Copyright (C) 2010 Christian Becke <christianbecke@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

from circular_permutations import circular_permutations

LOXPFWD = "ATAACTTCGTATAGCATACATTATACGAAGTTAT"
LOXPREV = "ATAACTTCGTATAATGTATGCTATACGAAGTTAT"

class SequenceError (Exception):

	def __init__ (self, srec):
		self.seq_record = srec
		Exception.__init__ (self)


class NoLoxSite (SequenceError):
	pass

class FwdAndRevLoxSite (SequenceError):
	pass


def has_loxp (srec):
	return (LOXPFWD in srec.seq.upper () or LOXPREV in srec.seq.upper ())


def has_loxp_fwd_and_rev (srec):
	return (LOXPFWD in srec.seq.upper () and LOXPREV in srec.seq.upper ())


def count_loxp (srec):
	return srec.seq.upper ().count (LOXPFWD) + srec.seq.upper ().count (LOXPREV)


def cre (*args):
	in_srecs = []
	for arg in args:
		in_srecs += decre (arg)

	seen_seqs = {}
	index_list = []
	for i in xrange (len (in_srecs)):
		k = str (in_srecs[i].seq)
		if not seen_seqs.has_key (k):
			seen_seqs[k] = i
		index_list.append (seen_seqs[k])

	out_srecs = []
	for p in circular_permutations (index_list):
		s = Seq ("")
		names = []
		i = 0
		for index in p:
			srec = in_srecs[index]
			i += 1
			s += srec.seq
			name = srec.annotations.get ("CreRecEMBL_name", None)
			if not name:
				name = "seq%02d" % (i,)
			names.append (name)
		s.alphabet = generic_dna
		combined_srec = SeqRecord (s)
		combined_srec.annotations["CreRecEMBL_name"] = "_x_".join (names)
		out_srecs.append (combined_srec)
	return out_srecs


def decre (srec):
	n_fwd = srec.seq.upper ().count (LOXPFWD)
	n_rev = srec.seq.upper ().count (LOXPREV)

	if n_fwd > 0 and n_rev > 0:
		raise FwdAndRevLoxSite (srec)

	need_revcomp = False
	if n_fwd > 0:
		sep = LOXPFWD
	elif n_rev > 0:
		sep = LOXPREV
		need_revcomp = True
	else:
		raise NoLoxSite (srec)

	out = []
	original_name = srec.annotations.get ("CreRecEMBL_name", "seq")
	count = 0
	parts = srec.seq.upper ().split (sep)
	parts[-1] += parts[0]
	parts = parts[1:]
	for p in parts:
		count += 1
		if need_revcomp:
			p = p.reverse_complement ()
		s = Seq (LOXPFWD) + p
		s.alphabet = generic_dna
		srec = SeqRecord (s)
		if len (parts) > 1:
			 name = "%s%02d" % (original_name, count)
		else:
			name = original_name
		srec.annotations["CreRecEMBL_name"] = name
		out.append (srec)
	return out
