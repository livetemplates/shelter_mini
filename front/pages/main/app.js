 let tg = window.Telegram.WebApp; 

   tg.expand(); 
   tg.MainButton.show()

tg.MainButton.text = "Donation";
tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#57aade';

  

 Telegram.WebApp.onEvent('mainButtonClicked', function(){
      tg.sendData("buy"); 
      
   });
   
   Telegram.WebApp.onEvent('backButtonClicked', function(){
      tg.close(); 
      
   });
