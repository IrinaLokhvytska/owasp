function error_alert(msg) {
    $('#show_alert #content').html(msg);
    $('#show_alert #alert_body').removeClass();
    $('#show_alert #alert_body').addClass("alert alert-danger");
    $('#show_alert .modal-dialog').addClass("modal-error");
    $('#show_alert').modal('show');

}

function look_for_error(response) {
    let get_error_msg = jQuery.parseJSON(response.responseText)["error"]
    if (get_error_msg) {
        error_alert(get_error_msg)
    }
    return true
}
