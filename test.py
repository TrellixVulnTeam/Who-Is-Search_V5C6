import unittest

class TestStringMethods(unittest.TestCase):

    def test_check(self):
        self.assertEqual(self.check_domain("google.com"), True)
        self.assertEqual(self.check_domain("google.net"), True)
        self.assertEqual(self.check_domain("google.org"), True)

    def check_domain(self,domain):
        if len(domain)<2: return False
        try:
            domain_split = domain.split(".")
            if len(domain_split)<2: return False
            if len(domain_split)>3: return False
            else:
                if len(domain_split[0])==0: return False
                tld=domain_split[1]
                if tld=="si": return True
                if tld=="com": return True
                if tld=="net": return True
                if tld=="org": return True
                if tld=="biz": return True
                else: return False
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    unittest.main()
