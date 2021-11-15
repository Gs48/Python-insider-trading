# Python-insider-trading
Insider trading data using python

The data is pulled from nseindia.com

Insider trading is considered one of the best way to take short time trades. Website upload data each day after 5pm-6pm IST

Changes to make in the code:

  i) Change dates to appropriate format = 21-12-2012
  ii) Website continuously changes its cookies, copy site cookies and paste it in headers
  
Key Notes:

  i) Above code considers stocks which have no pledged shares,if so insiders might be buying back. It gives only fresh buying from open markets
  ii) Code considers stocks which have buying only from open markets and not traded between insiders with their own
  iii) Consider stocks which have buying astleast more than ₹ 1 crore  
  
  
  
