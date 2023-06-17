from bs4 import BeautifulSoup
import requests

print("beautifulsoup4 is running & lxml is running & requests is running")

url = "https://ideabeam.com/finance/rates/goldprice.php"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

tags_td_title = doc.title
# print(tags_td_title.string)
platform_name = 'ideabeam'

tags_td_pawn = doc.find_all("td")[8]
# print(tags_td_pawn.string)
Gold_unit = tags_td_pawn.string

tags_td_price = doc.find_all("td")[9]
# print(tags_td_price.string)
Price_rs = tags_td_price.string

# with open('text.html','+r') as file_read:
#     print(f"open to read => text.html")
#     file = BeautifulSoup(file_read, 'html.parser')
#     tag_h1 = file.find_all('h1')[0]
#     print(tag_h1.string)
#     tag_h1.string = "sdf"


Html = f'<title>Text</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"crossorigin="anonymous"/><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script><div class="container"><h1 class="text-center fs-1 m-2">Gold price</h1><table class="table table-striped"><thead><tr><th scope="col">#</th><th scope="col">Platform</th><th scope="col">Gold unit</th><th scope="col">Price</th><th scope="col">Link</th></tr></thead><tbody><tr><th scope="row">1</th><td>{platform_name}</td><td>{Gold_unit}</td><td>{Price_rs}</td><td><a href="{url}" target="_blank">ideabeam</a></td></tr><!-- <tr><th scope="row">3</th><td colspan="2">Larry the Bird</td><td>@twitter</td></tr> --></tbody></table></div>'


""" Write the text.html """
with open("text.html", "+w") as file_writing:
    print(f"open to write => [{'text.html'}] ")
    writing = BeautifulSoup(file_writing, "html.parser")
    file_writing.write(Html)
    # print(f"{platform_name},{Gold_unit},{Price_rs}")
