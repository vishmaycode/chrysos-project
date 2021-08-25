function relod_page()
{
    window.location.reload();
    var invalue=$('#k_21_in').val();
            invalue=invalue/3012.00;
            $('#k_21_out').val(invalue);
}