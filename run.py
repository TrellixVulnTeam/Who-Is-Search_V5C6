# -*- coding: utf-8 -*-
import urllib.request
import os
import sys
import ParseHTML

class Whois:
    # SI register parameters which can be read from whois
    si_domain = None
    si_registrar = None
    si_registrar_url = None
    si_nameserver = []
    si_status = None
    si_created = None
    si_expire = None
    si_source = None
    si_domain_holder = None
    si_tech = None

    # COM NET ORG BIZ register parameters which can be read from whois
    com_Registry_Domain_ID = None
    com_Registrar_WHOIS_Server = None
    com_Registrar_URL = None
    com_Updated_Date = None
    com_Creation_Date = None
    com_Registrar_Registration_Expiration_Date = None
    com_Registrar = None
    com_Registrar_IANA_ID = None
    com_Reseller = None
    com_Domain_Status = []
    com_Registry_Registrant_ID = None
    com_Registrant_Name = None
    com_Registrant_Organization = None
    com_Registrant_Street = None
    com_Registrant_City = None
    com_Registrant_State_Province = None
    com_Registrant_Postal_Code = None
    com_Registrant_Country = None
    com_Registrant_Phone = None
    com_Registrant_Phone_Ext = None
    com_Registrant_Fax = None
    com_Registrant_Fax_Ext = None
    com_Registrant_Email = None
    com_Registry_Admin_ID = None
    com_Admin_Name = None
    com_Admin_Organization = None
    com_Admin_Street = None
    com_Admin_City = None
    com_Admin_State_Province = None
    com_Admin_Postal_Code = None
    com_Admin_Country = None
    com_Admin_Phone = None
    com_Admin_Phone_Ext = None
    com_Admin_Fax = None
    com_Admin_Fax_Ext = None
    com_Admin_Email = None
    com_Registry_Tech_ID = None
    com_Tech_Name = None
    com_Tech_Organization = None
    com_Tech_Street = None
    com_Tech_City = None
    com_Tech_State_Province = None
    com_Tech_Postal_Code = None
    com_Tech_Country = None
    com_Tech_Phone = None
    com_Tech_Phone_Ext = None
    com_Tech_Fax = None
    com_Tech_Fax_Ext = None
    com_Tech_Email = None
    com_Name_Server = []
    com_DNSSEC = None
    com_Registrar_Abuse_Contact_Email = None
    com_Registrar_Abuse_Contact_Phone = None

    #search content
    raw_whois_data = None

    def check_domain(self, domain):
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
                if tld=="de": return True
                if tld=="eu": return True
                if tld=="pl": return True
                if tld=="hr": return True
                if tld=="rs": return True
                else: return False
        except Exception as e:
            print(str(e))


    def search(self,domain):
        print(self.check_domain(domain))
        #search for whois data and send respod resp = urllib.request.urlopen(req)
        if self.check_domain(domain): #če je domena prave oblike
            
            try:
                url = 'https://www.whois.com/whois/'+domain
                # now, with the below headers, we defined ourselves as a simpleton who is
                # still using internet explorer.
                headers = {}
                headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
                req = urllib.request.Request(url, headers = headers)
                resp = urllib.request.urlopen(req)
                respData = resp.read()
                prvi_string=str(respData).split('\\n')

                name = domain.split(".")[0]
                tld = domain.split(".")[1]
                #print(self.parse_data_tld(respData))
                
                self.raw_whois_data = self.parse_data_tld(respData)
                print(self.__str__())
                
                #saveFile = open('HTML_content_'+domain+'.txt','w')
                #return prvi_string
                #saveFile.close()
            
            except Exception as e:
                print(str(e))
                
        else: return "null" #če domena ni prave oblike

    def parse_data_tld(self, content):
        # data in
        try:
            parser = ParseHTML.ParseHTML()
            html = content
            parser.feed(str(html))
            return parser.data
        except Exception as e:
            print(str(e))

    def __str__(self):
        string = ""
        for line in self.raw_whois_data:
            line_split = line.split('\\n')
            for item in line_split:
                string+=item+'\n'
        return string
        

        

#if __name__ == "__main__":
#    req=Whois()
#    req.search('najdi.si')
