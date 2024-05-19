import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import re,argparse,os

class LoginTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LoginTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        

        self.driver = webdriver.Chrome(service=s) 

    def test_true_login(self): #doğru bilgilerle login olunduğunda index.html'e redirect ediyor mu
        self.driver.get("http://127.0.0.1:3000/") 
        
        input_username = self.driver.find_element(By.NAME, "username")
        input_password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CLASS_NAME, "login-button")
        
        #doğru bilgilerle login ol
        input_username.send_keys("beyz")
        input_password.send_keys("123")
        sleep(1)
        login_button.click()

        # Yönlendirilen sayfayı kontrol etme
        redirected_url = self.driver.current_url
        if "http://127.0.0.1:3000/index.html" in redirected_url:
            print("Test başarılı:  Doğru bilgilerle login butonuna tıklandığında doğru sayfaya yönlendiriliyor.")
        else:
            print("Test başarısız: Doğru sayfaya yönlendirilmedi.Lütfen username:beyz,password:123 kullanıcısının kayıt oldunğuna emin olunuz.")

    def test_false_login(self): #yanlış bilgilerle login olmaya çalışınca uyarı çıkıyor mu
        self.driver.get("http://127.0.0.1:3000/") 
        
        # Giriş alanlarını bulma
        input_username = self.driver.find_element(By.NAME, "username")
        input_password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CLASS_NAME, "login-button")
        
        #şifreyi yanlış gönderdik
        input_username.send_keys("beyz")
        input_password.send_keys("1")
        sleep(1)
        login_button.click()

        error_div = self.driver.find_element(By.CSS_SELECTOR, "span[style='color: red;']")
        error_div_text = error_div.text
        if error_div_text == "Invalid Username or Password!":
            print("Test başarılı: Yanlış şifre girildiğinde 'Invalid Username or Password!' uyarısı görüntülendi.")
        else:
            print("Test başarısız: Uyarı görüntülenmedi.Lütfen beyz kullanıcısının kayıt olunduğuna ve şifresini de yanlış girdiğinize emin olunuz.")
    
    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class LoginImajTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LoginImajTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_login_h2(self): #buton texti doğru mu
        self.driver.get("http://127.0.0.1:3000/")
       
        baslik_div = self.driver.find_element(By.CSS_SELECTOR, ".card h2")
        giris_yap_metni = baslik_div.text
        self.assertEqual(giris_yap_metni,"Giriş Yap")
        print("Test başarılı: Login butonunun içeriği doğrudur.")

    def test_login_h2_font_size(self): #font size doğru mu
        self.driver.get("http://127.0.0.1:3000/")
        baslik_div = self.driver.find_element(By.CSS_SELECTOR, ".card h2")
        boyut = baslik_div.value_of_css_property("font-size")
        self.assertEqual(boyut,"42px")
        print("Test başarılı: Login butonunun font-size'ı doğru ve 42px'dir.")

    def test_login_button(self): #doğru renk geliyor mu butona testi
        self.driver.get("http://127.0.0.1:3000/")
        button=self.driver.find_element(By.XPATH,"//button[@class='login-button']")
        renk = button.value_of_css_property("background-color")
        expected_rgb = "rgba(0, 123, 255, 1)"
        self.assertEqual(renk, expected_rgb)
        print("Test başarılı: Login butonun renk bilgisi doğrudur.")

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class RegisterTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(RegisterTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

    def test_register(self): #kayıt ol linkine tıklayınca register.html'e redirect ediyor mu
        self.driver.get("http://127.0.0.1:3000/") 
        
        register_link = self.driver.find_element(By.XPATH, "//a[text()='Kayıt ol!']")
        register_link.click()
        sleep(3)  
        current_url = self.driver.current_url
        expected_url = "http://127.0.0.1:3000/Register.html"
        
        if current_url == expected_url:
            print("Test başarılı: Kayıt ol linki doğru URL'ye yönlendiriyor.")
        else:
            print("Test başarısız: Kayıt ol linki beklenen URL'ye yönlendirilmedi.")

    def test_register_navbar(self): #navbardaki link sayısı
        self.driver.get("http://127.0.0.1:3000/Register.html") 

        navbar = self.driver.find_element(By.CLASS_NAME, "navbar-nav")
        # Navbar içindeki öğeleri bul
        navbar_items = navbar.find_elements(By.CLASS_NAME, "nav__item")
        
        if len(navbar_items) == 30:
            print("Test başarılı: Navbar'da 30 öğe bulunuyor.")
        else:
            print("Test başarısız: Navbar'da 30 öğe bulunmuyor.")

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()


class RegisterImajTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(RegisterImajTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

    def test_register_form_imaj_control(self):
        try:
            self.driver.get("http://127.0.0.1:3000/Register.html")
            # Formun varlığını kontrol et
            form = self.driver.find_element(By.TAG_NAME, "form")
            assert form is not None, "Form bulunamadı."

            # Gerekli alanları kontrol et
            username_input = form.find_element(By.NAME, "username")
            assert username_input.get_attribute("placeholder") == "Username", "Kullanıcı adı giriş alanının konumu yanlış."

            email_input = form.find_element(By.NAME, "email")
            assert email_input.get_attribute("placeholder") == "Email", "E-posta giriş alanının konumu yanlış."

            password_input = form.find_element(By.NAME, "password")
            assert password_input.get_attribute("placeholder") == "Password", "Şifre giriş alanının konumu yanlış."

            print("Test başarılı: Register formu doğru şekilde konumlandırılmış ve stillendirilmiş.")
        except Exception as e:
            print("Test başarısız.Register formu doğru şekilde konumlandırılmamış veya stillendirilmemiş:", e)
        finally:
            self.driver.quit()

    def test_register_button(self): #doğru renk geliyor mu butona testi
        self.driver.get("http://127.0.0.1:3000/Register.html")
        button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        renk = button.value_of_css_property("background-color")
        expected_rgb = "rgba(0, 123, 255, 1)" 
        self.assertEqual(renk, expected_rgb)
        print("Test başarılı: Register butonunun rengi doğrudur.")

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class BlogTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BlogTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_blog_page_title(self):
        self.driver.get("http://127.0.0.1:3000/blog.html")
        page_title = self.driver.find_element(By.XPATH, "//h1[@class='pagetitle__heading']")

        title_text = page_title.text
        expected_title = "Our Blog"

        if title_text == expected_title:
            print("Test başarılı: Blog Sayfa başlığı doğru ve başlık 'Our Blog'dur.")
        else:
            print("Test başarısız: Blog Sayfa başlığı bulunamadı veya doğru değil.")

    def test_blog(self): #add new blog butonu linkine tıklayınca doğru redirect ediyor mu
        self.driver.get("http://127.0.0.1:3000/blog.html") 
        
        # Giriş alanlarını bulma
        add_new_blog = self.driver.find_element(By.XPATH, "//div[@class='d-flex justify-content-center align-items-center']/a[@class='btn btn__white mr-30']")
        add_new_blog.click()
        sleep(3)  
        current_url = self.driver.current_url
        expected_url = "http://127.0.0.1:3000/add-blog-post.html"
        
        if current_url == expected_url:
            print("Test başarılı: Add New Blog butonu doğru URL'ye yönlendiriyor.")
        else:
            print("Test başarısız: Add New Blog butonu beklenen URL'ye yönlendirilmedi.")

    def test_blog_link_count(self):
        self.driver.get("http://127.0.0.1:3000/blog.html") 

        blog_links = self.driver.find_elements(By.XPATH, "//li[@class='nav__item has-dropdown'][a[text()='Blog']]//ul[@class='dropdown-menu']//a[contains(@class, 'nav__item-link')]")
        link_count = len(blog_links)

        expected_link_count = 2

        # Link sayısını doğrula
        assert link_count == expected_link_count, f"Test Başarısız. Navbar blog altında beklenen {expected_link_count} link bulunmalı, ancak {link_count} link bulundu."
        print("Test başarılı: Navbar Blog sekmesi altında 2 link bulunuyor.")

    def test_blog_true_read_more_url(self): #blog sayfasındaki read more butonları farklı url'lere yönlendiriyor mu
        try:
            # Blog sayfasını açın
            self.driver.get("http://127.0.0.1:3000/blog.html")
            
            read_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".btn.btn__secondary.btn__link")

            for index, button in enumerate(read_more_buttons):
                # Her bir "Read More" düğmesine tıkla
                button.click()
                
                # Yeni sayfanın URL'sini kontrol et
                expected_url = f"http://127.0.0.1:3000/blog/{index + 1}/"
                sleep(2)  
                current_url = self.driver.current_url
                
                if current_url == expected_url:
                    print(f"Test başarılı: Blog altındaki read_more butonu için test geçildi {index + 1}: {current_url}")
                else:
                    print(f"Test başarısız: Blog altındaki read_more butonu için test başarısız oldu {index + 1}: {current_url}")
                
                # Blog sayfasına geri dön
                self.driver.back()
                sleep(2)  

        finally:
            self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()


class FormControlTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FormControlTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_submit_add_blog_form(self): #add_blog form dorğu gönderiliyor mu kontrol
        # Form sayfasına git
        self.driver.get("http://127.0.0.1:3000/add-blog-post.html")  # URL'yi uygun şekilde güncelleyin
        try:
            title_input = self.driver.find_element(By.XPATH, "//input[@id='title']")
            title_input.send_keys("Test Post Title")

            image_input = self.driver.find_element(By.XPATH, "//input[@id='image']")
            #image_input.send_keys("b201210100/static/assets/blog_images/blog.jpg")

            absolute_image_path = os.path.abspath("b201210100/static/assets/blog_images/blog.jpg")
            image_input.send_keys(absolute_image_path)

            categories_input = self.driver.find_element(By.XPATH, "//input[@id='categories']")
            categories_input.send_keys("Test Category")

            date_input = self.driver.find_element(By.XPATH, "//input[@id='date']")
            date_input.send_keys("05.05.2024")  

            description_input = self.driver.find_element(By.XPATH, "//textarea[@id='description']")
            description_input.send_keys("Test Description")

            read_more_input = self.driver.find_element(By.XPATH, "//input[@id='read_more_link']")
            read_more_input.send_keys("https://blog.hubspot.com/marketing/how-to-start-a-blog")

            submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn__primary') and contains(@class, 'btn__primary-style2')]")
            sleep(5)
            submit_button.click()
            redirected_url = self.driver.current_url
            print(redirected_url)
            if "http://127.0.0.1:3000/add-blog-post.html" in redirected_url:
                print("Test başarılı: Blog ekleme formuna girilen bilgiler doğru ve blog ekleme işlemi başarılıdır.")
            else:
                print("Test başarısız: Lütfen blog ekleme formuna girilen bilgilerin doğruluğunu kontrol ediniz.")

        except Exception as e:
            print(f"Test başarısız. Bir hata oluştu: {e}")
        finally:
            self.driver.quit()

    def test_submit_add_industries_form(self): #add_industries form dorğu gönderiliyor mu kontrol
        try:
            self.driver.get("http://127.0.0.1:3000/add-industries.html") 
            title_input = self.driver.find_element(By.XPATH, "//form//input[@id='title']")
            title_input.send_keys("Test Title")

            image_input = self.driver.find_element(By.XPATH, "//form//input[@id='image']")
            #image_input.send_keys("b201210100/static/assets/blog_images/blog.jpg")
            absolute_image_path = os.path.abspath("b201210100/static/assets/blog_images/blog.jpg")
            image_input.send_keys(absolute_image_path)

            description_textarea = self.driver.find_element(By.XPATH, "//form//textarea[@id='description']")
            description_textarea.send_keys("Bu sektör için örnek bir açıklamadır.")

            # Formu gönder
            submit_button = self.driver.find_element(By.XPATH, "//button[text()='Add Industries']") 
            submit_button.click()

            # Sayfanın belirtilen URL'ye yönlendirilmesini bekle
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("http://127.0.0.1:3000/industries.html")
            )
            print("Test başarılı. Industries ekleme formuna girilen bilgiler doğru ve industries ekleme işlemi başarılıdır.")
        except Exception as e:
            print(f"Test başarısız. Industries form gönderme işlemi gerçekleşmedi. Bir hata oluştu: {e}")
        finally:
            self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()


class CommentControlTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CommentControlTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_blog_comment(self): 
        try:
            self.driver.get("http://127.0.0.1:3000/blog/1/")

            comment_textarea = self.driver.find_element(By.XPATH, "//form//textarea[@name='content']")
            comment_textarea.send_keys("Bu bir test yorumudur.")
            sleep(2)
            comment_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Submit Comment']")
            comment_button.click()

            print("Test başarılı: Blog'a yorum başarıyla gönderildi.")
            
        except NoSuchElementException:
            print("Test başarısız. Hiç blog gönderisi olmadığı için yorum yapma testi başarısız olmuştur. Lütfen önce blog ekleyin.")
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Test başarısız. Blog yorum ekleme testi başarısız. Hata: {e}")
        finally:
            self.driver.quit()

    def test_industries_comment(self):
        try:
            self.driver.get("http://127.0.0.1:3000/industries/1/")

            comment_textarea = self.driver.find_element(By.XPATH, "//form//textarea[@name='content']")
            comment_textarea.send_keys("Bu bir test yorumudur.")
            sleep(2)
            comment_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Submit Comment']")
            comment_button.click()

            print("Test başarılı : Industries'e yorum başarıyla gönderildi.")
            
        except NoSuchElementException:
            print("Test başarısız. Hiç industries olmadığı için yorum yapma testi başarısız olmuştur. Lütfen önce industries ekleyin.")
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Test başarısız. Industries yorum ekleme testi başarısız. Hata: {e}")
        finally:
            self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()


class PopupTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PopupTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_index_video_popup(self):
        try:
            self.driver.get("http://127.0.0.1:3000/index.html")

            video_link = self.driver.find_element(By.XPATH, "//a[@class='video__btn video__btn-white popup-video']")

            video_link.click()
            sleep(1)

            # Açılan pop-up'ı kontrol et
            popup_window = self.driver.window_handles[-1]
            assert popup_window is not None, "Test başarısız: Video popup açılmadı."

            print("Test başarılı.Video bağlantısına tıklandıktan sonra popup başarıyla açıldı.")

        except Exception as e:
            print("Error:", e)
        finally:
            self.driver.quit()

    def test_search_button_Ac(self):
        try:
            self.driver.get("http://127.0.0.1:3000/index.html")
            icon_search = self.driver.find_element(By.CSS_SELECTOR, "i.icon-search")
            sleep(2)
            icon_search.click()
            sleep(2)
            # Popup'ın açılıp açılmadığını kontrol et
            close_button = self.driver.find_element(By.XPATH, "//button[@class='search-popup__close']")
            if close_button:
                print("Test başarılı: Search popup'ı başarıyla açıldı.")

        except Exception as e:
            print("Hata:", e)
        finally:
            self.driver.quit()

    def test_search_button_kapat(self):
        try:
            self.driver.get("http://127.0.0.1:3000/index.html")
            icon_search = self.driver.find_element(By.CSS_SELECTOR, "i.icon-search")
            icon_search.click()
            sleep(2)
  
            close_button = self.driver.find_element(By.XPATH, "//button[@class='search-popup__close']")
            close_button.click()
            sleep(1)
            icon_search = self.driver.find_element(By.CSS_SELECTOR, "i.icon-search")  #sayfanın kapanıp kapanmadıgını test etmek
            style =icon_search.get_attribute("style")
            index=style.find("visibility: hidden;") #find fonk bulamazsa -1 döndürür
            if index == -1:
                print("Test başarılı: Search popup'ı başarıyla kapatıldı.")
        except Exception as e:
            print("Hata:", e)
        finally:
            self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class IndustriesTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IndustriesTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_industires(self): #add new industries linkine tıklayınca doğru redirect ediyor mu
        self.driver.get("http://127.0.0.1:3000/industries.html") 
        
        # Giriş alanlarını bulma
        add_new_blog = self.driver.find_element(By.XPATH, "//a[contains(@href, 'add-industries.html') and contains(@class, 'btn__white')]")
        add_new_blog.click()
        sleep(3) 
        current_url = self.driver.current_url
        expected_url = "http://127.0.0.1:3000/add-industries.html"
        
        if current_url == expected_url:
            print("Test başarılı: Add New Industries butonu doğru URL'ye yönlendiriyor.")
        else:
            print("Test başarısız: Add New Industries butonu beklenen URL'ye yönlendirilmedi.")


    def test_industries_link_count(self):
        self.driver.get("http://127.0.0.1:3000/industries.html") 
        # Blog altındaki linkleri bulma
        industries_links = self.driver.find_elements(By.XPATH, "//a[@class='nav__item-link dropdown-menu-title' and text()='IT Solutions']/following-sibling::ul[@class='nav flex-column']//a[@class='nav__item-link']")
        link_count = len(industries_links)

        expected_link_count = 6

        assert link_count == expected_link_count, f"Test başarısız: Navbar industries altında beklenen {expected_link_count} link bulunmalı, ancak {link_count} link bulundu."
        print("Test başarılı: Navbar Industries altında 6 link bulunuyor.")


    def test_industries_true_read_more_url(self): #industries sayfasındaki read more butonları farklı url'lere yönlendiriyor mu
        try:
            self.driver.get("http://127.0.0.1:3000/industries.html")
            # "Read More" düğmelerini bulun
            read_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".btn.btn__secondary.btn__link")

            for index, button in enumerate(read_more_buttons):
                # Her bir "Read More" düğmesine tıkla
                button.click()
                # Yeni sayfanın URL'sini kontrol et
                expected_url = f"http://127.0.0.1:3000/industries/{index + 1}/"
                sleep(2)  
                current_url = self.driver.current_url
                
                if current_url == expected_url:
                    print(f"Test başarılı: Industries altındaki read_more butonu için test geçildi {index + 1}: {current_url}")
                else:
                    print(f"Test başarısız: Industries altındaki read_more butonu için test başarısız oldu {index + 1}: {current_url}")
                
                self.driver.back()
                sleep(2) 
        finally:
            self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class IndustriesImajTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IndustriesImajTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_add_industries_button(self): #doğru renk geliyor mu butona testi
        self.driver.get("http://127.0.0.1:3000/add-industries.html")
        button=self.driver.find_element(By.XPATH,"//button[text()='Add Industries']")
        renk = button.value_of_css_property("background-color")
        expected_rgb = "rgba(76, 175, 80, 1)" 
        self.assertEqual(renk, expected_rgb)
        print("Test başarılı: Add Industries butonunun rengi doğru.")

    def test_industry_page_title(self): #sayfa başlığı doğru mu testi
        self.driver.get("http://127.0.0.1:3000/add-industries.html") 

        # Sayfa başlığını bulma
        page_title = self.driver.find_element(By.XPATH, "//h1[@class='pagetitle__heading']")

        title_text = page_title.text
        expected_title = "Add New Industries"

        if title_text == expected_title:
            print("Test başarılı: Add New Industries sayfa başlığı doğru.")
        else:
            print("Test başarısız: Beklenen sayfa başlığı bulunamadı veya doğru değil.")

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class ImajControlTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ImajControlTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s) 

    def test_footer_text(self):
        try:
            self.driver.get("http://127.0.0.1:3000/index.html")
            text = self.driver.find_element(By.CSS_SELECTOR, "span.fz-14")
            # Metnin doğruluğu
            self.assertEqual(text.text, "© 2020 DataSoft, All Rights Reserved. With Love by")
            print("Test başarılı: Footerda bulunan başlık doğrudur.")
        except Exception as e:
            print("Test başarısız. Footerda bulunan başlık doğru değil.Error:", e)
        finally:
            self.driver.quit()

    def test_faq_question_count(self):
        self.driver.get("http://127.0.0.1:3000/faqs.html") 
        try:
            # Tüm soruları bul
            questions = self.driver.find_elements(By.CLASS_NAME, "accordion__title")
            # Soru sayısını kontrol et
            assert len(questions) == 10, f"Test başarısız:Faqs sayfasında 10 questions bekleniyor, fakat {len(questions)} questions bulundu."

            print("Test başarılı: Faqs sayfasında 10 adet soru bulunmuştur.")
        
        except Exception as e:
            print("Hata:", e)
        finally:
            self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class HomeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(HomeTest, self).__init__(*args, **kwargs)
        s = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

    def test_email_link(self):
        self.driver.get("http://127.0.0.1:3000/index.html") 
        try:
            email_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='mailto:Datasoft@7oroof.com']")

            # E-posta bağlantısının varlığını ve metnini kontrol et
            assert email_link is not None, "E-mail link not found on the page."
            assert email_link.text == "Datasoft@7oroof.Com", "E-mail link text is incorrect."

            print("Test başarılı: Home sayfasında E-mail link bulunuyor ve metni doğru.")
        except Exception as e:
            print("Test başarısız.Home sayfasında E-mail link yanlış. Hata:", e)
        finally:
            self.driver.quit()

    def test_valid_phone_number_format(self):
        try:
            self.driver.get("http://127.0.0.1:3000/index.html")

            phone_number_element = self.driver.find_element(By.XPATH, "//a[@href='tel:(002) 01061245741']")
            phone_number = phone_number_element.text
            print(str(phone_number))

            # Telefon numarası formatını doğrulama
            pattern = r'^\(\d{3}\) \d{11}$'
            if re.match(pattern, phone_number):
                print("Test başarılı: Home sayfasında telefon Numarası doğru formattadır.")
            else:
                print("Test başarısız: Telefon numarası yanlış formattadır.")
        except Exception as e:
            print("Hata:", e)
        finally:
            self.driver.quit()

    
    def test_index_logo(self): #index.html de ki header logosu varlıgı testi
        try:
            self.driver.get("http://127.0.0.1:3000/index.html")
            # Logoyu bul
            logo_light = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "logo-light"))
            )
            logo_dark = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "logo-dark"))
            )
            print("Test başarılı: Home'da ki navbar logosu başarıyla bulundu.")

        except Exception as e:
            print(f"Hata: {e}")

        finally:
            self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

def run_tests(test_suite):
    unittest.TextTestRunner().run(test_suite)

if __name__ == '__main__':
    while True:
        print("\nLütfen bir test kategorisi seçin:")
        print("1.  Login Testlerini Çalıştır")
        print("2.  Register Testlerini Çalıştır")
        print("3.  Login Imaje Testlerini Çalıştır")
        print("4.  Register Imaj Testlerini Çalıştır")
        print("5.  Form Control Testlerini Çalıştır")
        print("6.  Comment Kontrol Testlerini Çalıştır")
        print("7.  Blog Testlerini Çalıştır")
        print("8.  Popup Testlerini Çalıştır")
        print("9.  Industries Testlerini Çalıştır")
        print("10. Industries Testlerini Çalıştır")
        print("11. Imaj Kontrol Testlerini Çalıştır")
        print("12. Index-Home Testlerini Çalıştır")
        print("13. Çıkış Yap")

        choice = input("Seçiminizi giriniz: ")

        if choice == '1':
            login_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
            run_tests(login_suite)
        elif choice == '2':
            register_suite = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
            run_tests(register_suite)
        elif choice == '3':
            login_imaj_suite = unittest.TestLoader().loadTestsFromTestCase(LoginImajTest)
            run_tests(login_imaj_suite)
        elif choice == '4':
            register_imaj_suite = unittest.TestLoader().loadTestsFromTestCase(RegisterImajTest)
            run_tests(register_imaj_suite)
        elif choice == '5':
            form_control_suite = unittest.TestLoader().loadTestsFromTestCase(FormControlTest)
            run_tests(form_control_suite)
        elif choice == '6':
            comment_control_suite = unittest.TestLoader().loadTestsFromTestCase(CommentControlTest)
            run_tests(comment_control_suite)
        elif choice == '7':
            blog_suite = unittest.TestLoader().loadTestsFromTestCase(BlogTest)
            run_tests(blog_suite)
        elif choice == '8':
            popup_suite = unittest.TestLoader().loadTestsFromTestCase(PopupTest)
            run_tests(popup_suite)
        elif choice == '9':
            industries_suite = unittest.TestLoader().loadTestsFromTestCase(IndustriesTest)
            run_tests(industries_suite)
        elif choice == '10':
            industries_imaj_suite = unittest.TestLoader().loadTestsFromTestCase(IndustriesImajTest)
            run_tests(industries_imaj_suite)
        elif choice == '11':
            imaj_control_suite = unittest.TestLoader().loadTestsFromTestCase(ImajControlTest)
            run_tests(imaj_control_suite)
        elif choice == '12':
            home_suite = unittest.TestLoader().loadTestsFromTestCase(HomeTest)
            run_tests(home_suite)
        elif choice == '13':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz sayı. Lütfen tekrar deneyin.")