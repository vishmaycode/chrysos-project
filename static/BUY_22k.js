function relod_page() {
    window.location.reload();
    var invalue = $('#k_22_in').val();
    invalue = invalue / 3012.00;
    $('#k_22_out').val(invalue);
}