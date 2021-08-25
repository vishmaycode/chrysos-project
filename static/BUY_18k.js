function relod_page()
{
    window.location.reload();
    var invalue=$('#k_18_in').val();
    invalue=invalue/3012.00;
    $('#k_18_out').val(invalue);
}