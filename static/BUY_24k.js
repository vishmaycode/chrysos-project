function relod_page()
{
    window.location.reload();
    var invalue=$('#k_24_in').val();
            invalue=invalue/3012.00;
            $('#k_24_out').val(invalue);
}