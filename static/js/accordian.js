$(window).on('load',function(){
 

  
   // $.ajax({
   //     url:  '/policyViewmat/'+id_ob+'/',
   //     type: "GET",
   //     dataType: "json",
   //     data:{"menubar":ackdetail},
   //     success: function(response){
   //     }
   //   })

})


function matapi(idd, fileid, page)
{
  //alert(idd)

   var nested = '#'+idd
  var ackdetail =  $('#ackdetail').val()
  var ackdetailId =  $('#ackdetailtype').val()
  document.getElementById("pagination").focus();
  //alert(ackdetailId)
  $.ajax({
       url:  '/policyViewmat/',
       type: "GET",
       dataType: "json",
       // data:{"menubar":ackdetail},
       data:{"menubar":ackdetail, "file_type" : fileid,"mainId": ackdetailId,"page": page},
       success: function(response){
        //alert(JSON.stringify(response['pagination']))
       $(nested).empty()
       $('#pagination').html('')
         for (var i=0; i<response['policy'].length;i++)
            {
              $(nested).append(`<li style="padding-top:4%"><input type="checkbox" id="c_${response['policy'][i]['id']}" onclick="megafolders(this.id, ${fileid}); " /> <label for="c_${response['policy'][i]['id']}" class="tree_label tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['policy'][i]['submenu_name']}</span></label><ul class="nested" id="nested_${response['policy'][i]['id']}" ></ul></li>`)
              //$(nested).append(`<li style="padding-top:4%"><input type="checkbox" id="c_${response[i]['id']}" onclick="megafolder(this.id,${response[i]['file_type']}); " /> <label for="c_${response[i]['id']}" class="tree_label tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response[i]['submenu_name']}</span></label><ul class="nested" id="nestedmat_${response[i]['id']}" ></ul></li>`)
            }
            for (var j=0; j<response['obj'].length;j++)
            {
             // $(nested).append(`<li><label for="c_${response['obj'][j]['id']}" class=" tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['obj'][j]['submenu_name']}</span></label></li>`)
            }

          var pagi_length =response['pagination']['numpages']+1
          if (response['pagination']['numpages'] > 0)
          {
            
            if (response['pagination']['know_user_changes'] == true)
            {
              //alert("ok")
              $('#pagination').append(`<a href="#">&laquo;</a>`)
              if(response['pagination']['know_previous']==true){
                $('#pagination').append(`<a href="#" onclick="matapi('${idd}','${fileid}',${response['pagination']['know_previous_page']})">prev</a>`)
              }

              for (var i=1;i<pagi_length;i++)
               {
                if (response['pagination']['current_page']==i)
                {
                    
                   $('#pagination').append(`<a href="#" class="selected active">${i}</a>`)
                }  
                else{
                    
                   $('#pagination').append(`<a href="#" class="paginate" id="${i}" onclick="matapi('${idd}','${fileid}','${i}');">${i}</a>`)
                }
               }
               if (response['pagination']['know_next']==true)
                       {
                           $('#pagination').append(`<a href="#" onclick="matapi('${idd}','${fileid}',${response['pagination']['know_next_page_number']});">next</a>`)
                       }

            }
          }
       }
     })
}

//////////////////////////////////////without reload/////////
function megafolder(idd,fileid)
{
  //nested_
  var ackdetail =  $('#ackdetail').val()
  var id_obj = idd.split("_")
  var id_ob = id_obj[1]
  if (fileid==1)
  {var nested = '#nested_'+id_ob
  }
  else
  {var nested = '#nestedmat_'+id_ob
  }
  
  var image = '#img_'+id_ob
  $.ajax({
       url:  '/policyView/'+id_ob+'/',
       type: "GET",
       dataType: "json",
       data:{"menubar":ackdetail, "file_type" : fileid},
       success: function(response){
        

         //var total = response['policy'].length + response['obj'].length-1
        
         $(nested).empty()
         for (var i=0; i<response['policy'].length;i++)
            {
             
                if (response['policy'][i]['id'] != id_ob)
                {
                  
                  $(nested).append(`<li><input type="checkbox" id="c_${response['policy'][i]['id']}" onclick="megafolders(this.id, ${fileid}); " /> <label for="c_${response['policy'][i]['id']}" class="tree_label tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['policy'][i]['submenu_name']}</span></label><ul class="nested" id="nested_${response['policy'][i]['id']}" ></ul></li>`)
                }
            
            }
            for (var j=0; j<response['obj'].length;j++)
            {
              $(nested).append(`<li><label for="c_${response['obj'][j]['id']}" class=" tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['obj'][j]['submenu_name']}</span></label></li>`)
            }
           
        }
     })
}

function megafolders(idd, fileid)
{

  var ackdetail =  $('#ackdetail').val()
  var i;
  var id_obj = idd.split("_")
  var id_ob = id_obj[1]
  var nested = '#nested_'+id_ob
  //alert(nested)
  $.ajax({
       url:  '/policyView/'+id_ob+'/',
       type: "GET",
       dataType: "json",
       data:{"menubar":ackdetail, "file_type" : fileid},
       success: function(response){
        
         $(nested).empty()
         for (var i=0; i<response['policy'].length;i++)
            {
             
                if (response['policy'][i]['id'] != id_ob)
                {
                  $(nested).append(`<li><input type="checkbox" id="c_${response['policy'][i]['id']}" onclick="megafolders(this.id); " /> <label for="c_${response['policy'][i]['id']}" class="tree_label tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['policy'][i]['submenu_name']}</span></label><ul class="nested" id="nested_${response['policy'][i]['id']}" ></ul></li>`)
                }
            
            }
            for (var j=0; j<response['obj'].length;j++)
            {
              $(nested).append(`<li><label for="c_${response['obj'][j]['id']}" class=" tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['obj'][j]['submenu_name']}</span></label></li>`)
            }
           
        }
     })
}
