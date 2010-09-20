# vim: fileencoding=utf-8 ts=4 sw=4 noexpandtab :

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


import itertools
import operator


class circular_tuple (tuple):

	def _find_best (self, t, best_list, offset):
		best_index = best_list[0]
		best_value = t[best_index + offset]
		ambigous = False
		for index in best_list[1:]:
			if t[index + offset] < best_value:
				best_value = t[index + offset]
				best_index = index
			elif t[index + offset] == best_value:
				ambigous = True
		if ambigous:
			return None
		else:
			return best_index


	def _find_start (self, t, indices):
		weighted = []
		n = 1
		current = indices[0]
		weight = 1
		while n < len (indices):
			if indices[n] == current + 1:
				weight += 1
			else:
				weighted.append ((current, weight))
				current = indices[n]
				weight = 1
			n += 1
		weighted.append ((current, weight))

		if 0 in indices and len (t) - 1 in indices:
			(first, first_weight) = weighted.pop (0)
			(last, last_weight) = weighted.pop (-1)
			last_weight += first_weight
			weighted.append ((last, last_weight))

		weighted.sort (key=operator.itemgetter (1), reverse=True)

		best = []
		(index, best_weight) = weighted[0]
		best.append (index)
		for (index, weight) in weighted[1:]:
			if weight < best_weight:
				break
			best.append (index)
		
		for i in xrange (len (t) - 1):
			best_index = self._find_best (t, best, -(i + 1))
			if best_index is not None:
				break
		
		if best_index is None:
			best_index = best[0]
		
		return best_index


	def _find_all (self, t, needle):
		indices = []
		pos = t.index (needle)
		while pos != -1:
			indices.append (pos)
			try:
				pos = t.index (needle, pos + 1)
			except ValueError:
				pos = -1
		return indices


	def _normalize (self, t):
		if len (t) > 0:
			l = list (t)
			l.sort ()
			needle = l[0]
			indices = self._find_all (t, needle)
			start = self._find_start (t, indices)
			return t[start:] + t[:start]
		else:
			return t


	def __hash__ (self):
		t = self._normalize (self)
		return t.__hash__ ()


	def __eq__ (self, item):
		if not isinstance (item, circular_tuple):
			raise ValueError
		t1 = self._normalize (self)
		t2 = self._normalize (item)
		return tuple (t1) == tuple (t2) 



def circular_permutations (iterable):
	p = itertools.permutations (iterable)
	seen = set ()
	for e in p:
		e = circular_tuple (e)
		if e in seen:
			continue
		seen.add (e)
		yield e

