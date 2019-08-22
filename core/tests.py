from django.test import TestCase

class AnoBissextoTestCase(TestCase):

    def verSeAnoEBissexto(self, ano):
        return True if ((ano % 4 == 0 and ano % 100 != 0) or (
                    ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0)) else False

    def test_identifica_anos_bissextos_corretos(self):
        """Avalia se o algororitmo é capaz de reconhecer devidamente anos bissextos"""

        self.assertEqual(self.verSeAnoEBissexto(1600), True)
        self.assertEqual(self.verSeAnoEBissexto(1732), True)
        self.assertEqual(self.verSeAnoEBissexto(1888), True)
        self.assertEqual(self.verSeAnoEBissexto(1944), True)
        self.assertEqual(self.verSeAnoEBissexto(2008), True)

    def test_identifica_anos_bissextos_incorretos(self):
        """Avalia se o algororitmo é capaz de reconhecer devidamente anos que não são bissextos"""
        self.assertEqual(self.verSeAnoEBissexto(1742), False)
        self.assertEqual(self.verSeAnoEBissexto(1889), False)
        self.assertEqual(self.verSeAnoEBissexto(1951), False)
        self.assertEqual(self.verSeAnoEBissexto(2011), False)
        self.assertEqual(self.verSeAnoEBissexto(2009), False)