// Get the form values
var ticker = $('input[name="ticker"]').val();

// Send the POST request to the server

$.ajax({
  type: 'POST',
  url: '/get-stock-info',
  data: JSON.stringify({ ticker: ticker }),
  contentType: 'application/json',
  success: function(data) {
    // Update the page with the new stock information
//    $('#stock-price').text(data.stockPrice);
//    $('#volatility').text(data.volatility);
//    $('#historical-high').text(data.historicalHigh);
//    $('#historical-low').text(data.historicalLow);
  }
});