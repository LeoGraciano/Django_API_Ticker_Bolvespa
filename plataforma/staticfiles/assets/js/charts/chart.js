$(function () {
    var ticker = function () {

        $('#myChart').remove();
            $('#box-chart').append('<canvas id="myChart" width="400" height="400"></canvas>');
        var card = $(this);
        $('.ticker svg.fa-check').addClass('d-none');


        $.ajax({
            url: card.attr("data-url"),
            type: 'get',
            dataType: 'json',
            success: function (data) {
                card.find('svg.fa-check').removeClass('d-none')
                var result = data['result']
                var month = ['jan', 'feb', 'mar', 'abr', 'mai', 'jun', 'jul', 'aug', 'set', 'oct', 'nov', 'dec']
                var dt = [];
                var close = [];

                result.forEach(element => {
                    let d = new Date(element['dt'])
                    dt.push(`${month[d.getMonth()]} ${d.getDay()}`)
                    close.push(element['close'])

                });

                var coloR = [];

                var dynamicColors = function () {
                    var r = Math.floor(Math.random() * 255);
                    var g = Math.floor(Math.random() * 255);
                    var b = Math.floor(Math.random() * 255);
                    return "rgb(" + r + "," + g + "," + b + ")";
                };

                for (let index = 0; index < dt.length; index++) {
                    coloR.push(dynamicColors())

                }
                var ctx = document.getElementById('myChart').getContext('2d');
                var myChart = new Chart(ctx, {

                    type: 'line',
                    data: {
                        labels: dt,
                        datasets: [{
                            label: data['label'],
                            data: close,
                            backgroundColor: coloR,
                            borderColor: coloR,
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true
                                }
                            }]
                        }
                    }
                });
            }
        });
    }




    $('.ticker').click(ticker);

});