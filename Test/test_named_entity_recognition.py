import unittest
import named_entity_recognition

text = "Happy Zoo Year! The new trailer for Zootopia featuring Shakira’s new single “Try Everything, is here!" \
       " Watch now and see the film in theatres in 3D March 4! The modern mammal metropolis of Zootopia is a city " \
       "like no other. Comprised of habitat neighborhoods like ritzy Sahara Square and frigid Tundratown, it’s a melting" \
       " pot where animals from every environment live together—a place where no matter what you are, from the biggest " \
       "elephant to the smallest shrew, you can be anything. But when rookie Officer Judy Hopps (voice of Ginnifer Goodwin)" \
       " arrives, she discovers that being the first bunny on a police force of big, tough animals isn’t so easy. Determined" \
       " to prove herself, she jumps at the opportunity to crack a case, even if it means partnering with a fast-talking," \
       " scam-artist fox, Nick Wilde (voice of Jason Bateman), to solve the mystery. Walt Disney Animation Studios’ “Zootopia,”" \
       " a comedy-adventure directed by Byron Howard and Rich Moore and co-directed by Jared Bush, opens in theaters on March 4," \
       " 2016. Like Zootopia on Facebook - https://www.facebook.com/DisneyZootopia Follow @DisneyZootopia on Twitter - " \
       "https://twitter.com/disneyzootopia Follow @DisneyAnimation on Instagram - https://twitter.com/disneyanimation Follow " \
       "Disney Animation on Tumblr - http://disneyanimation.tumblr.com/ Category Film & Animation"


class TestStringMethods(unittest.TestCase):

    def test_ner(self):
        ne = named_entity_recognition.recognition(text)
        self.assertEqual(ne, ['zootopia', 'shakira', 'mammal metropolis',
                              'tundratown', 'rookie', 'judy hopps', 'ginnifer goodwin',
                              'fox', 'nick wilde', 'jason bateman', 'zootopia', 'byron howard',
                              'rich moore', 'jared bush', 'zootopia']
                         )


if __name__ == '__main__':
    unittest.main()
