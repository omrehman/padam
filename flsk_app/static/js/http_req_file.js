 var response_div;
function getXMLHttp()
{
  var xmlHttp

  try
  {
    //Firefox, Opera 8.0+, Safari
    xmlHttp = new XMLHttpRequest();
  }
  catch(e)
  {
    //Internet Explorer
    try
    {
      xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
    }
    catch(e)
    {
      try
      {
        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
      }
      catch(e)
      {
        alert("Your browser does not support AJAX!")
        return false;
      }
    }
  }
  return xmlHttp;
}

function MakeRequest(site_adress,resp_div)
{
  var xmlHttp = getXMLHttp();
  response_div = resp_div;
  xmlHttp.onreadystatechange = function()
  {
    if(xmlHttp.readyState == 4)
    {
      HandleResponse(xmlHttp.responseText);
    }
  }
     
  xmlHttp.open("GET", site_adress, true); 
  xmlHttp.send(null);
}

function HandleResponse(response)
{
  var result = "<table>";
  var word = response.split("#");
  for(i = 0 ; i< word.length; i++)
      {
         var word_and_sense = word[i].split("?");
            
            result+= "<td><label>"+word_and_sense[0]+"</label></td>";
            
          if(word_and_sense.length >2)
              {
                    result+="<tr>"
                    var words = word_and_sense[1].split("@");
                     
                     for(j = 0 ; j<words.legth;j++)
                         {
                             
                             var word_text = words[j].split("*"); 
                             result+="<td>\n\
                          <table><tr><td>\n\
                                         <input type='text' readonly value='"+word_text[1]+"'      \n\
                                  </td>\n\
                                    <td> <input type='radio' name='sense' value='"+word_text[0]+"'> </td> </tr>";        
                             
                         }//FOR LOOP ENDS [ for(j = 0 ; j<words.legth;j++) ]
                     
                           
              }//IF ENDS [ if(word_and_sense.length >2) ]
              else
                  {
                      if(word_and_sense[0].length!="")
                          {
                                result+="<td> <input type='text' id='transliterateTextarea5' name='new_word' > </td>";
                          }//IF ENDS [ if(word_and_sense[0]!="") ]
                  }//ELSE ENDS [ if(word_and_sense.length >2) ]
           
                result+="</tr>";
          //result = result+word_and_sense[0]+" "+word_and_sense.length+"<br>";
          
      }//FOR LOOP ENDS [ for(i = 0 ; i< word.length; i++) ]
      
      result+= "</table>";
  document.getElementById(response_div).innerHTML = result;
}


