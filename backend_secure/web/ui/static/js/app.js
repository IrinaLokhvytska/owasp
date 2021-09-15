$(document).ready(function () {
    $('[id^="filter_input_"]').on("keyup", function () {
        var table_id = $(this).attr("id").replace("filter_input_", "")
        var value = $(this).val().toLowerCase();
        $("#table_" + table_id + " tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});