#Import modules
import unittest
import festival_scheduler

class test_festival_methods():
	#Test when there are festivals
	def test_select_festival(self):
		location = 'Austin'
		genre = 'Rock'
		test_possible_festivals = select_festival(location, genre, global_festivals_list)

		for festival in test_possible_festivals:
			self.AssertEqual(festival.location, location)
			self.AssertIn(genre, festival.genres)
  
	#test that there are no results (-1)
	def test_no_results(self):
		location = 'NotReal'
		genre = 'FakeNews'
		test_possible_festivals = select_festival(location, genre, global_festivals_list)

		self.AssertEqual(test_possible_festivals, -1)

if __name__ == '__main__':
	unittest.main()