import dryscrape
from bs4 import BeautifulSoup


sess = dryscrape.Session(base_url='http://www.amazon.in')
sess.visit('http://www.amazon.in/United-Colors-Benetton-Flip-Flops-Slippers/dp/B014CZA8P0/ref=pd_rhf_se_s_qp_1?_encoding=UTF8&pd_rd_i=B014CZA8P0&pd_rd_r=04RP223D4SF9BW7S2NP1&pd_rd_w=ZgGL6&pd_rd_wg=0PSZe&refRID=04RP223D4SF9BW7S2NP1')
sess.set_header('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
html = sess.body()
soup = BeautifulSoup(html)
print(soup)