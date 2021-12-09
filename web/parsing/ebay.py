import re
from typing import List

from bs4 import BeautifulSoup
import requests
from concurrent.futures import as_completed, ThreadPoolExecutor
from parsing.models import Ebay, ImportExcels


def get_page_item_urls(in_url) -> List[str]:
    # check some data before returning url, return only good items
    # return urls of items from listing
    soup = BeautifulSoup(requests.get(in_url).content.decode(), 'lxml')
    ebay_ = soup.find('div', class_="srp-river-results clearfix").find_all('li', class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")
    ebay_items = []

    for ebay in ebay_:
        try:
            url = ebay.find('div', class_='s-item__wrapper clearfix').find('div', class_='s-item__info clearfix').find('a').get('href')
        except:
            url = ''

        ebay_items.append(url)
    return ebay_items


def get_page_detail(url) -> dict:
    soup = BeautifulSoup(requests.get(url).content.decode(), 'lxml')
    data = {'url': url}

    try:
        title = soup.find('h1', id='itemTitle').text.strip('Details about')

    except:
        title = ''
    data['title'] = title

    try:
        condition = soup.find('div', id='vi-itm-cond').text

    except:
        condition = ''
    data['condition'] = condition

    try:
        quantity = soup.find('span', id='qtySubTxt').text.strip()
        n_quantity = re.findall(r'\b\d+\b', quantity)
        quantity = int(n_quantity[0]) if len(n_quantity) else 0

    except:
        quantity = 0
    data['quantity'] = quantity

    try:
        star = soup.find('span', class_='mbg-l').find('a').text
        n_star = re.findall(r'\b\d+\b', star)
        star = int(n_star[0]) if len(n_star) else 0
    except:
        star = 0
    data['star'] = star

    try:
        percent = soup.find('div', id='si-fb').text
        n_percent = re.findall(r'\b\d+\b', percent)
        percent = int(n_percent[0]) if len(n_percent) else 0

    except:
        percent = 0
    data['percent'] = percent


    try:
        location = soup.find('span', itemprop='availableAtOrFrom').text.split()[-1]

    except:
        location = ''
    data['location'] = location

    return data


def ebay_main(instance=None):
    if instance:
        title = instance.title.replace(' ', '+')

        ebay_urls = [f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={title}&_sacat=0',]
    else:
        ebay_urls = [
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Concealer++Warm+Light+0.2+++Oz+&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Julep+Eyeshadow+101+Cr%C3%A8me+to+Powder+Waterproof+Eyeshadow+Stick+Stone&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Multi-Use+Concealer+Light++0.2+Oz+&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Concealer++Warm+Light+0.2+++Oz+&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Softsoap+Liquid+Hand+Soap%2C+Fresh+Breeze++7.5+Oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Multi-Use+Concealer+Light++0.2+Oz+&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Julep+Eyeshadow+101+Cr%C3%A8me+to+Powder+Waterproof+Eyeshadow+Stick+Stone&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Softsoap+Liquid+Hand+Soap%2C+Fresh+Breeze++7.5+Oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+New+York+Fit+Me+Liquid+Concealer+Makeup+Soft+Tan+0.46+oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Julep+Eyeshadow+101+Cr%C3%A8me+to+Powder+Waterproof+Eyeshadow+Stick+Stone&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Cuccio+Naturale+Sweet+Almond+Cuticle+Oil++75ml+Yellow&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+New+York+Fit+Me+Liquid+Concealer+Makeup+Soft+Tan+0.46+oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+SuperStay+Ink+Crayon+Matte+Longwear+Lipstick+With+Built-in+Sharpener%2C+Treat+Yourself%2C+0.04+Ounce&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Cuccio+Naturale+Sweet+Almond+Cuticle+Oil++75ml+Yellow&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+SuperStay+Ink+Crayon+Matte+Longwear+Lipstick+With+Built-in+Sharpener%2C+Treat+Yourself%2C+0.04+Ounce&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+SuperStay+Ink+Crayon+Matte+Longwear+Lipstick+With+Built-in+Sharpener%2C+Treat+Yourself%2C+0.04+Ounce&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Denman+Hair+Brush+for+Curly+Hair+D5+&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+SuperStay+Ink+Crayon+Matte+Longwear+Lipstick+With+Built-in+Sharpener%2C+Treat+Yourself%2C+0.04+Ounce&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=e.l.f.+16HR+Camo+Concealer++Full+Coverage+%26+Highly+Pigmented+Matte+Finish+Medium+Warm+&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Denman+Hair+Brush+for+Curly+Hair+D5+&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=NYX+PROFESSIONAL+MAKEUP+Precision+Eyebrow+Pencil+Black&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=e.l.f.+16HR+Camo+Concealer++Full+Coverage+%26+Highly+Pigmented+Matte+Finish+Medium+Warm+&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Oreal+Paris+Makeup+Infallible+Never+Fail+Original+Mechanical+Pencil+Eyeliner+with+Built+in+Sharpener++Brown+0.008+oz.&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=NYX+PROFESSIONAL+MAKEUP+Precision+Eyebrow+Pencil+Black&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+SuperStay+24%2C+2-Step+Liquid+Lipstick%2C+Coffee+Edition%2C+Chai+Once+More&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Oreal+Paris+Makeup+Infallible+Never+Fail+Original+Mechanical+Pencil+Eyeliner+with+Built+in+Sharpener++Brown+0.008+oz.&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+SuperStay+24%2C+2-Step+Liquid+Lipstick%2C+Infinite+Petal&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+SuperStay+24%2C+2-Step+Liquid+Lipstick%2C+Coffee+Edition%2C+Chai+Once+More&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Rimmel+Magnif%27+Eye+Liner%2C+Brown%2C+2+Count&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+SuperStay+24%2C+2-Step+Liquid+Lipstick%2C+Infinite+Petal&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=l%27oreal+paris+superior+preference+fade-defying+%2B+shine+permanent+hair+color%2C+5g+medium+golden+brown%2C+pack+of+3%2C+hair+dye&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=l%27oreal+paris+superior+preference+fade-defying+%2B+shine+permanent+hair+color%2C+5g+medium+golden+brown%2C+pack+of+3%2C+hair+dye&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Oreal+Paris+Superior+Preference+Fade-Defying+%2B+Shine+Permanent+Hair+Color%2C+6AM+Light+Amber+Brown+&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=l%27oreal+paris+superior+preference+fade-defying+%2B+shine+permanent+hair+color%2C+5g+medium+golden+brown%2C+pack+of+3%2C+hair+dye&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+New+York+Super+Stay+Full+Coverage+Liquid+Foundation+Makeup%2C+340+Cappuccino%2C+1+Fl+Oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Oreal+Paris+Superior+Preference+Fade-Defying+%2B+Shine+Permanent+Hair+Color%2C+6AM+Light+Amber+Brown+&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+Super+Stay+Full+Coverage+Liquid+Foundation+Makeup%2C+Toffee%2C+1+Fl+Oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+New+York+Super+Stay+Full+Coverage+Liquid+Foundation+Makeup%2C+340+Cappuccino%2C+1+Fl+Oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+New+York+Liquid+Foundation+Makeup%2C+Full+Coverage+Liquid+and+Up+To+24+Hour+Wear%2C+Soft+Matte+Finish%2C+Medium+Beige%2C+129+MEDIUM+BEIGE%2C+1.0+Ounce&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+Super+Stay+Full+Coverage+Liquid+Foundation+Makeup%2C+Toffee%2C+1+Fl+Oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Garnier+Hair+Color+Olia+Oil+Powered+Permanent%2C+7.0+Dark+Blonde%2C+2+Count&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+New+York+Liquid+Foundation+Makeup%2C+Full+Coverage+Liquid+and+Up+To+24+Hour+Wear%2C+Soft+Matte+Finish%2C+Medium+Beige%2C+129+MEDIUM+BEIGE%2C+1.0+Ounce&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Australian+Gold+Botanical+Sunscreen+Tinted+Face+BB+Cream+SPF+50%2C+3+Ounce+%7C+Medium-Tan+%7C+Broad+Spectrum+%7C+Water+Resistant+%7C+Vegan+%7C+Antioxidant+Rich&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Garnier+Hair+Color+Olia+Oil+Powered+Permanent%2C+7.0+Dark+Blonde%2C+2+Count&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Revlon+Root+Erase+Permanent+Hair+Color%2C+At-Home+Root+Touchup+Hair+Dye+with+Applicator+Brush+for+Multiple+Use%2C+100%25+Gray+Coverage%2C+Dark+Brown+%284%29%2C+3.2+oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=garnier+olia+oil+powered+permanent+hair+color%2C+5.0+medium+brown+%28packaging+may+vary%29%2C+2+count&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Dove+Skin+Care+Beauty+Bar+For+Softer+Skin+Cucumber+And+Green+Tea+More+Moisturizing+Than+Bar+Soap+3.75+oz%2C+8+Bars&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Revlon+Root+Erase+Permanent+Hair+Color%2C+At-Home+Root+Touchup+Hair+Dye+with+Applicator+Brush+for+Multiple+Use%2C+100%25+Gray+Coverage%2C+Dark+Brown+%284%29%2C+3.2+oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Or%C3%A9al+Paris+True+Match+Super-Blendable+Powder%2C+Buff+Beige%2C+0.33+oz.%2CN4+Buff+Beige%2CK1601203&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Dove+Skin+Care+Beauty+Bar+For+Softer+Skin+Cucumber+And+Green+Tea+More+Moisturizing+Than+Bar+Soap+3.75+oz%2C+8+Bars&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Aveeno+Apple+Cider+Vinegar+Clarifying+In-Shower+Hair+Rinse+for+Balance+%26+Shine%2C+Sulfate+Free+Gentle+pH-Balancing+Hair+Treatment+for+Oily+or+Dull+Hair%2C+Paraben+%26+Dye-Free%2C+6.8+Fl+Oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Or%C3%A9al+Paris+True+Match+Super-Blendable+Powder%2C+Buff+Beige%2C+0.33+oz.%2CN4+Buff+Beige%2CK1601203&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=rimmel+natural+bronzer+sun+light%2C+0.49+ounce+%28pack+of+2%29&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Rimmel+Natural+Bronzer+Sun+Light%2C+0.49+Ounce+%28Pack+of+3%29&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Oreal+Paris+Age+Perfect+Radiant+Serum+Foundation+with+SPF+50%2C+Warm+Beige%2C+1+Ounce&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=rimmel+natural+bronzer+sun+light%2C+0.49+ounce+%28pack+of+2%29&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+Color+Sensational+Lipstick%2C+Lip+Makeup%2C+Cream+Finish%2C+Hydrating+Lipstick%2C+Nude%2C+Pink%2C+Red%2C+Plum+Lip+Color%2C+Plum+Perfect%2C+0.15+oz%3B+%28Packaging+May+Vary%29&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Oreal+Paris+Age+Perfect+Radiant+Serum+Foundation+with+SPF+50%2C+Warm+Beige%2C+1+Ounce&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Goody+Ouchless+Value+Pack+Heather+Scrunchies%2C+12ct&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+Color+Sensational+Lipstick%2C+Lip+Makeup%2C+Cream+Finish%2C+Hydrating+Lipstick%2C+Nude%2C+Pink%2C+Red%2C+Plum+Lip+Color%2C+Plum+Perfect%2C+0.15+oz%3B+%28Packaging+May+Vary%29&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Alaffia+Authentic+African+Black+Soap+All-in-One%2C+Tangerine+Citrus%2C+32+Oz.+Body+Wash%2C+Facial+Cleanser%2C+Shampoo%2C+Shaving%2C+Hand+Soap.+Perfect+for+All+Skin+Types.+Fair+Trade%2C+No+Parabens%2C+Cruelty+Free%2C+Vegan&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Goody+Ouchless+Value+Pack+Heather+Scrunchies%2C+12ct&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Tree+Hut+24+Hour+Intense+Hydrating+Shea+Body+Butter+++Almond+and+Honey++7+Ounce&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Alaffia+Authentic+African+Black+Soap+All-in-One%2C+Tangerine+Citrus%2C+32+Oz.+Body+Wash%2C+Facial+Cleanser%2C+Shampoo%2C+Shaving%2C+Hand+Soap.+Perfect+for+All+Skin+Types.+Fair+Trade%2C+No+Parabens%2C+Cruelty+Free%2C+Vegan&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Old+Spice+Red+Collection+After+Hours+Scent+Deodorant+for+Men%2C+3.0+oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Tree+Hut+24+Hour+Intense+Hydrating+Shea+Body+Butter+++Almond+and+Honey++7+Ounce&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Oreal+Paris+Makeup+Infallible+Super+Slim+Long-Lasting+Liquid+Eyeliner%2C+Ultra-Fine+Felt+Tip%2C+Quick+Drying+Formula%2C+Glides+on+Smoothly%2C+Grey%2C+Pack+of+1&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Old+Spice+Red+Collection+After+Hours+Scent+Deodorant+for+Men%2C+3.0+oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Dove+Beauty+Bar+More+Moisturizing+Than+Traditional+Bar+Soaps+Coconut+Milk+++3.75+oz+&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Oreal+Paris+Makeup+Infallible+Super+Slim+Long-Lasting+Liquid+Eyeliner%2C+Ultra-Fine+Felt+Tip%2C+Quick+Drying+Formula%2C+Glides+on+Smoothly%2C+Grey%2C+Pack+of+1&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+New+York+Brow+Tattoo+Longlasting+Tint%2C+Dark+Brown%2C+4.9+ml&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Dove+Beauty+Bar+More+Moisturizing+Than+Traditional+Bar+Soaps+Coconut+Milk+++3.75+oz+&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Julep+When+Pencil+Met+Gel+Long-Lasting+Waterproof+Gel+Eyeliner%2C+Electric+Teal+Shimmer&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+New+York+Brow+Tattoo+Longlasting+Tint%2C+Dark+Brown%2C+4.9+ml&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Rimmel+Stay+Matte+Liquid+Foundation%2C+Warm+Beige%2C+1+Fl+Oz%2C+Pack+of+2&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Julep+When+Pencil+Met+Gel+Long-Lasting+Waterproof+Gel+Eyeliner%2C+Electric+Teal+Shimmer&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Oreal+Paris+Cosmetics+Magic+BB+Cream+Anti-Redness%2C+2+Count&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Rimmel+Stay+Matte+Liquid+Foundation%2C+Warm+Beige%2C+1+Fl+Oz%2C+Pack+of+2&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=BIC+Flex+5+Titanium+Men%27s+Disposable+Razor%2C+Five+Blade%2C+Pack+of+10+Razors%2C+Flexible+Blades+for+an+Ultra-Close+Shave&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Oreal+Paris+Cosmetics+Magic+BB+Cream+Anti-Redness%2C+2+Count&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Kirk%27s+Original+Coco+Castile+Bar+Soap+Fragrance+Free+4+Ounces+%288+Pack%29&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=BIC+Flex+5+Titanium+Men%27s+Disposable+Razor%2C+Five+Blade%2C+Pack+of+10+Razors%2C+Flexible+Blades+for+an+Ultra-Close+Shave&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Or%C3%A9al+Paris+Makeup+Magic+Skin+Beautifier+BB+Cream+Tinted+Moisturizer+Face+Makeup%2C+Anti-Redness%2C+Green%2C+1+fl.+oz.&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Kirk%27s+Original+Coco+Castile+Bar+Soap+Fragrance+Free+4+Ounces+%288+Pack%29&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Oreal+Paris+Colorista+1-Day+Washable+Temporary+Hair+Color+Spray%2C+Gold%2C+2+Ounces&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Or%C3%A9al+Paris+Makeup+Magic+Skin+Beautifier+BB+Cream+Tinted+Moisturizer+Face+Makeup%2C+Anti-Redness%2C+Green%2C+1+fl.+oz.&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=L%27Oreal+Paris+Colorista+1-Day+Washable+Temporary+Hair+Color+Spray%2C+Mint%2C+2+Ounces&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Oreal+Paris+Colorista+1-Day+Washable+Temporary+Hair+Color+Spray%2C+Gold%2C+2+Ounces&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=CloSYS+Ultra+Sensitive+Mouthwash++Unflavored++%2C+32+&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=L%27Oreal+Paris+Colorista+1-Day+Washable+Temporary+Hair+Color+Spray%2C+Mint%2C+2+Ounces&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=bareMinerals+Barepro+Performance+Wear+Powder+Foundation%2C+Warm+Natural%2C+0.34+Ounce&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=CloSYS+Ultra+Sensitive+Mouthwash++Unflavored++%2C+32+&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=bareMinerals+BAREPRO+Performance+Wear+Pressed+Powder+Foundation%2C+Light+Natural+09%2C+0.34+oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=bareMinerals+Barepro+Performance+Wear+Powder+Foundation%2C+Warm+Natural%2C+0.34+Ounce&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Maybelline+Color+Sensational+Lipstick++Pitch+Black%2C+0.15+oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=bareMinerals+BAREPRO+Performance+Wear+Pressed+Powder+Foundation%2C+Light+Natural+09%2C+0.34+oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=e.l.f.+Glossy+Gloss++Sweet+Salmon+0.08++&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=Maybelline+Color+Sensational+Lipstick++Pitch+Black%2C+0.15+oz&_osacat=0&_sop=10&LH_PrefLoc=1&_fcid=1',
    ]

    items_data = []  # items from details page
    urls = []  # urls from listing page

    with ThreadPoolExecutor(max_workers=10) as executor:
        # todo: if many list pages with urls in them, use thread pool executor too to parse urls concurrently
        futures = {executor.submit(get_page_item_urls, url): url for url in ebay_urls}  # list urls -> 50 urls
        for future in as_completed(futures):
            url = futures[future]
            try:
                data = future.result()
                urls.extend(data)
                print('parsed listing urls -> ', len(data), data)
            except Exception as exc:
                pass
                # print('%r generated an exception: %s' % (data, exc))


        future_to_url = {executor.submit(get_page_detail, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                items_data.append(data)
                print('parsed item -> ', data)
            except Exception as exc:
                pass
                # print('%r generated an exception: %s' % (data, exc))

        # print(len(items_data), '-------------------------------------------------')

    # # filtering and saving to database
    for item in items_data:
        """ Filtering conditions:
        condition = new and new with box
        quantity = > 10
        star = > 100
        % = > 98%
        """
        if item['star'] < 100:
            continue
        elif item['quantity'] < 10:
            continue
        elif item['condition'].lower() not in ['new', 'new with box']:
            continue
        elif item['percent'] < 98:
            continue
        elif item['location'].lower() not in ['states']:
            continue
        Ebay.objects.update_or_create(url=item['url'],  product_title_id=instance.id, defaults={'title': item['title']})   # время 0.26358866691589355

        # print(len(urls))
    return urls


