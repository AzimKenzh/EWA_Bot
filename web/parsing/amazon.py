from typing import List

import requests
from bs4 import BeautifulSoup

from concurrent.futures import as_completed, ThreadPoolExecutor

from parsing.models import Amazon

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
    'Accept-Language': "en-gb",
    'Accept-Encoding': 'br, gzip, deflate',
    'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}


def get_page_item_urls(html) -> List[dict]:
    soup = BeautifulSoup(requests.get(html, headers=headers).content.decode(), 'lxml')
    amazon_ = soup.find_all('div',
                            class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

    amazon_items = []

    for amazon in amazon_:
        title = amazon.find('span', class_='a-size-base-plus a-color-base a-text-normal').text
        try:
            url = f"https://www.amazon.com{amazon.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-4').find('a').get('href')}"
        except:
            url = ''

        data = {'url': url, 'title': title}
        amazon_items.append(data)
    return amazon_items


TITLES_AMAZON = ['maybelline instant age rewind eraser dark circles treatment concealer', 'maybelline instant age rewind eraser dark circles treatment multi-use', 'softsoap liquid hand soap, fresh breeze  7.5 oz', 'julep eyeshadow 101',
                 'maybelline new york superstay', 'cuccio naturale sweet almond cuticle oil', 'maybelline superstay ink crayon matte longwear lipstick with built-in sharpener', 'denman hair brush', 'e.l.f. 16hr camo concealer', 'nyx professional makeup precision',
                 "l'oreal paris makeup infallible never", 'maybelline superstay 24, 2-step liquid lipstick, coffee edition, chai once more', 'maybelline superstay 24, 2-step liquid lipstick, infinite petal', "rimmel magnif' eye liner, brown",
                 "l'oreal paris superior preference fade-defying + shine permanent hair color", 'maybelline new york super stay full coverage liquid foundation makeup', 'maybelline super stay full coverage liquid foundation makeup', 'maybelline new york liquid',
                 'garnier hair color olia oil powered permanent', 'australian gold botanical sunscreen tinted face bb cream spf 50, 3 ounce', 'garnier olia oil powered permanent hair color, 5.0 medium brown',
                 'revlon root erase permanent hair color, at-home root touchup hair dye with applicator brush for multiple use, 100% gray coverage', 'dove skin care beauty bar for softer skin cucumber and green tea more moisturizing than bar soap 3.75 oz',
                 "l'oréal paris true match super-blendable powder", 'aveeno apple cider vinegar', 'rimmel natural bronzer', "l'oreal paris age perfect radiant serum foundation with spf 50",
                 'maybelline color sensational lipstick, lip makeup, cream finish, hydrating lipstick, nude, pink, red, plum lip color', 'goody ouchless value', 'alaffia authentic african black soap all-in-one', 'tree hut 24 hour intense hydrating shea body butter',
                 'old spice red collection', "l'oreal paris makeup infallible super slim long-lasting liquid eyeliner, ultra-fine felt tip, quick drying formula", 'dove beauty bar more moisturizing than', 'maybelline new york brow tattoo', 'julep when pencil met gel long-lasting waterproof gel eyeliner',
                 'rimmel stay matte liquid foundation', "l'oreal paris cosmetics magic bb cream", 'bic flex 5', "kirk's original coco castile bar soap", "l'oréal paris makeup magic skin beautifier bb", "l'oreal paris colorista 1-day washable temporary hair color",
                 "l'oreal paris colorista 1-day washable temporary hair color spray", 'closys ultra sensitive mouthwash', 'bareminerals barepro performance wear powder foundation', 'maybelline color sensational lipstick', 'e.l.f. glossy gloss  sweet'
                 ]


def check_title(in_title: str) -> bool:
    for title_item in TITLES_AMAZON:
        if title_item in in_title.lower():
            return True
    return False


def amazon_main():
    amazons_url = ['https://www.amazon.com/s?k=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Concealer+Warm+Light+0.2+Oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Multi-Use+Concealer+Light+0.2+Oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Softsoap+Liquid+Hand+Soap%2C+Fresh+Breeze+7.5+Oz&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=Julep+Eyeshadow+101+Cr%C3%A8me+to+Powder+Waterproof+Eyeshadow+Stick+Stone&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=Maybelline+New+York+Fit+Me+Liquid+Concealer+Makeup+Soft+Tan+0.46+oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Cuccio+Naturale+Sweet+Almond+Cuticle+Oil+75ml+Yellow&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+SuperStay+Ink+Crayon+Matte+Longwear+Lipstick+With+Built-in+Sharpener%2C+Treat+Yourself%2C+0.04+Ounce&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Denman+Hair+Brush+for+Curly+Hair+D5&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=e.l.f.+16HR+Camo+Concealer+Full+Coverage+%26+Highly+Pigmented+Matte+Finish+Medium+Warm&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=NYX+PROFESSIONAL+MAKEUP+Precision+Eyebrow+Pencil+Black&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Makeup+Infallible+Never+Fail+Original+Mechanical+Pencil+Eyeliner+with+Built+in+Sharpener+Brown+0.008+oz.&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+SuperStay+24%2C+2-Step+Liquid+Lipstick%2C+Coffee+Edition%2C+Chai+Once+More&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+SuperStay+24%2C+2-Step+Liquid+Lipstick%2C+Infinite+Petal&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=Rimmel+Magnif%27+Eye+Liner%2C+Brown%2C+2+Count&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Superior+Preference+Fade-Defying+%2B+Shine+Permanent+Hair+Color%2C+5G+Medium+Golden+Brown%2C+Pack+of+3%2C+Hair+Dye&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Superior+Preference+Fade-Defying+%2B+Shine+Permanent+Hair+Color%2C+6AM+Light+Amber+Brown&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+New+York+Super+Stay+Full+Coverage+Liquid+Foundation+Makeup%2C+340+Cappuccino%2C+1+Fl+Oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+Super+Stay+Full+Coverage+Liquid+Foundation+Makeup%2C+Toffee%2C+1+Fl+Oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+New+York+Liquid+Foundation+Makeup%2C+Full+Coverage+Liquid+and+Up+To+24+Hour+Wear%2C+Soft+Matte+Finish%2C+Medium+Beige%2C+129+MEDIUM+BEIGE%2C+1.0+Ounce&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Garnier+Hair+Color+Olia+Oil+Powered+Permanent%2C+7.0+Dark+Blonde%2C+2+Count&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Australian+Gold+Botanical+Sunscreen+Tinted+Face+BB+Cream+SPF+50%2C+3+Ounce+%7C+Medium-Tan+%7C+Broad+Spectrum+%7C+Water+Resistant+%7C+Vegan+%7C+Antioxidant+Rich&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Garnier+Olia+Oil+Powered+Permanent+Hair+Color%2C+5.0+Medium+Brown+%28Packaging+May+Vary%29%2C+2+Count&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Revlon+Root+Erase+Permanent+Hair+Color%2C+At-Home+Root+Touchup+Hair+Dye+with+Applicator+Brush+for+Multiple+Use%2C+100%25+Gray+Coverage%2C+Dark+Brown+%284%29%2C+3.2+oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Dove+Skin+Care+Beauty+Bar+For+Softer+Skin+Cucumber+And+Green+Tea+More+Moisturizing+Than+Bar+Soap+3.75+oz%2C+8+Bars&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Or%C3%A9al+Paris+True+Match+Super-Blendable+Powder%2C+Buff+Beige%2C+0.33+oz.%2CN4+Buff+Beige%2CK1601203&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Aveeno+Apple+Cider+Vinegar+Clarifying+In-Shower+Hair+Rinse+for+Balance+%26+Shine%2C+Sulfate+Free+Gentle+pH-Balancing+Hair+Treatment+for+Oily+or+Dull+Hair%2C+Paraben+%26+Dye-Free%2C+6.8+Fl+Oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Rimmel+Natural+Bronzer+Sun+Light%2C+0.49+Ounce+%28Pack+of+2%29&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Age+Perfect+Radiant+Serum+Foundation+with+SPF+50%2C+Warm+Beige%2C+1+Ounce&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+Color+Sensational+Lipstick%2C+Lip+Makeup%2C+Cream+Finish%2C+Hydrating+Lipstick%2C+Nude%2C+Pink%2C+Red%2C+Plum+Lip+Color%2C+Plum+Perfect%2C+0.15+oz%3B+%28Packaging+May+Vary%29&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Goody+Ouchless+Value+Pack+Heather+Scrunchies%2C+12ct&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=Alaffia+Authentic+African+Black+Soap+All-in-One%2C+Tangerine+Citrus%2C+32+Oz.+Body+Wash%2C+Facial+Cleanser%2C+Shampoo%2C+Shaving%2C+Hand+Soap.+Perfect+for+All+Skin+Types.+Fair+Trade%2C+No+Parabens%2C+Cruelty+Free%2C+Vegan&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Tree+Hut+24+Hour+Intense+Hydrating+Shea+Body+Butter+Almond+and+Honey+7+Ounce&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Old+Spice+Red+Collection+After+Hours+Scent+Deodorant+for+Men%2C+3.0+oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Makeup+Infallible+Super+Slim+Long-Lasting+Liquid+Eyeliner%2C+Ultra-Fine+Felt+Tip%2C+Quick+Drying+Formula%2C+Glides+on+Smoothly%2C+Grey%2C+Pack+of+1&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Dove+Beauty+Bar+More+Moisturizing+Than+Traditional+Bar+Soaps+Coconut+Milk+3.75+oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+New+York+Brow+Tattoo+Longlasting+Tint%2C+Dark+Brown%2C+4.9+ml&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=Julep+When+Pencil+Met+Gel+Long-Lasting+Waterproof+Gel+Eyeliner%2C+Electric+Teal+Shimmer&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Rimmel+Stay+Matte+Liquid+Foundation%2C+Warm+Beige%2C+1+Fl+Oz%2C+Pack+of+2&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Cosmetics+Magic+BB+Cream+Anti-Redness%2C+2+Count&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=BIC+Flex+5+Titanium+Men%27s+Disposable+Razor%2C+Five+Blade%2C+Pack+of+10+Razors%2C+Flexible+Blades+for+an+Ultra-Close+Shave&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Kirk%27s+Original+Coco+Castile+Bar+Soap+Fragrance+Free+4+Ounces+%288+Pack%29&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Or%C3%A9al+Paris+Makeup+Magic+Skin+Beautifier+BB+Cream+Tinted+Moisturizer+Face+Makeup%2C+Anti-Redness%2C+Green%2C+1+fl.+oz.&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Colorista+1-Day+Washable+Temporary+Hair+Color+Spray%2C+Gold%2C+2+Ounces&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=L%27Oreal+Paris+Colorista+1-Day+Washable+Temporary+Hair+Color+Spray%2C+Mint%2C+2+Ounces&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=CloSYS+Ultra+Sensitive+Mouthwash+Unflavored+%2C+32&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=bareMinerals+Barepro+Performance+Wear+Powder+Foundation%2C+Warm+Natural%2C+0.34+Ounce&ref=nb_sb_noss_2',
                   'https://www.amazon.com/s?k=bareMinerals+BAREPRO+Performance+Wear+Pressed+Powder+Foundation%2C+Light+Natural+09%2C+0.34+oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=Maybelline+Color+Sensational+Lipstick+Pitch+Black%2C+0.15+oz&ref=nb_sb_noss',
                   'https://www.amazon.com/s?k=e.l.f.+Glossy+Gloss+Sweet+Salmon+0.08&ref=nb_sb_noss',
                   ]

    parsed_items = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(get_page_item_urls, url): url for url in amazons_url}
        for future in as_completed(futures):
            url = futures[future]
            try:
                data = future.result()
                parsed_items.extend(data)
            except Exception as exc:
                pass
                # print('%r generated an exception: %s' % (url, exc))

    for item in parsed_items:
        print(item['title'], 'title')
        if check_title(item['title']):
            print('found', item['url'])
            Amazon.objects.update_or_create(url=item['url'], defaults={'title': item['title']})
        else:
            print('not found', item['url'])

        # print(len(parsed_items), '-----------------------') # 1729 -----------------------

    return parsed_items



















# ["Maybelline Instant Age Rewind Eraser Dark Circles Treatment Concealer", "Maybelline Instant Age Rewind Eraser Dark Circles Treatment Multi-Use", "Softsoap Liquid Hand Soap, Fresh Breeze  7.5 Oz",
#  "Julep Eyeshadow 101", "Maybelline New York SuperStay", "Cuccio Naturale Sweet Almond Cuticle Oil", "Maybelline SuperStay Ink Crayon Matte Longwear Lipstick With Built-in Sharpener",
#  "Denman Hair Brush", "e.l.f. 16HR Camo Concealer", "NYX PROFESSIONAL MAKEUP Precision", "L'Oreal Paris Makeup Infallible Never", "Maybelline SuperStay 24, 2-Step Liquid Lipstick, Coffee Edition, Chai Once More",
#  "Maybelline SuperStay 24, 2-Step Liquid Lipstick, Infinite Petal", "Rimmel Magnif' Eye Liner, Brown", "L'Oreal Paris Superior Preference Fade-Defying + Shine Permanent Hair Color", "Maybelline New York Super Stay Full Coverage Liquid Foundation Makeup",
#  "Maybelline Super Stay Full Coverage Liquid Foundation Makeup", "Maybelline New York Liquid", "Garnier Hair Color Olia Oil Powered Permanent",
#  "Australian Gold Botanical Sunscreen Tinted Face BB Cream SPF 50, 3 Ounce", "Garnier Olia Oil Powered Permanent Hair Color, 5.0 Medium Brown", "Revlon Root Erase Permanent Hair Color, At-Home Root Touchup Hair Dye with Applicator Brush for Multiple Use, 100% Gray Coverage",
#  "Dove Skin Care Beauty Bar For Softer Skin Cucumber And Green Tea More Moisturizing Than Bar Soap 3.75 oz", "L'Oréal Paris True Match Super-Blendable Powder", "Aveeno Apple Cider Vinegar",
#  "Rimmel Natural Bronzer", "L'Oreal Paris Age Perfect Radiant Serum Foundation with SPF 50", "Maybelline Color Sensational Lipstick, Lip Makeup, Cream Finish, Hydrating Lipstick, Nude, Pink, Red, Plum Lip Color",
#  "Goody Ouchless value", "Alaffia Authentic African Black Soap All-in-One", "Tree Hut 24 Hour Intense Hydrating Shea Body Butter", "Old Spice Red Collection", "L'Oreal Paris Makeup Infallible Super Slim Long-Lasting Liquid Eyeliner, Ultra-Fine Felt Tip, Quick Drying Formula",
#  "Dove Beauty Bar More Moisturizing Than", "Maybelline New York Brow Tattoo", "Julep When Pencil Met Gel Long-Lasting Waterproof Gel Eyeliner", "Rimmel Stay Matte Liquid Foundation",
#  "L'Oreal Paris Cosmetics Magic BB Cream", "BIC Flex 5", "Kirk's Original Coco Castile Bar Soap", "L'Oréal Paris Makeup Magic Skin Beautifier BB", "L'Oreal Paris Colorista 1-Day Washable Temporary Hair Color",
#  "L'Oreal Paris Colorista 1-Day Washable Temporary Hair Color Spray", "CloSYS Ultra Sensitive Mouthwash", "bareMinerals Barepro Performance Wear Powder Foundation",
#  "Maybelline Color Sensational Lipstick", "e.l.f. Glossy Gloss  Sweet"
#  ]

