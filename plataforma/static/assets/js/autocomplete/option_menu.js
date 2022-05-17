function option_menu() {
    var s = $('#id_ticker').val();
    var option = new Array();
    if (s == '' || s.length < 3) { 
        return option
    }
    var option = [];
    $.ajax({
        url: '/ticker-search/',
        type: 'get',
        dataType: 'json',
        data: {
            term: s
        },
        success: function (data) {
            if (data.result.length > 0) {
                for (var i = 0; i < data.result.length; i++) {
                    option.push(`${data.result[i][0]}   `)
                }
            }
            return option
        }
    });


    }