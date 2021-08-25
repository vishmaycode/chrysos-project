$(document).ready(function(e){
    $("#selection button").click(function()
    {
        if(this.id == '24k')
        {
            
            $('#24k_para').addClass("show").removeClass("hide");
            $('#22k_para').addClass("hide");
            $('#21k_para').addClass("hide");
            $('#18k_para').addClass("hide");

        }
        else
        if(this.id == '22k')
        {
         $('#24k_para').addClass("hide");
         $('#22k_para').addClass("show").removeClass("hide");
         $('#21k_para').addClass("hide");
         $('#18k_para').addClass("hide");   

         }
        else
        if(this.id == '21k')
        {
         $('#24k_para').addClass("hide");
         $('#22k_para').addClass("hide");
         $('#21k_para').addClass("show").removeClass("hide");
         $('#18k_para').addClass("hide");

        }
        else
        if(this.id == '18k')
        {
         $('#24k_para').addClass("hide");
            $('#22k_para').addClass("hide");
            $('#21k_para').addClass("hide");
            $('#18k_para').addClass("show").removeClass("hide");
        
            
        }
    });
 });