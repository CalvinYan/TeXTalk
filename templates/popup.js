function onClick() {
   var record = document.getElementById('record');
   record.style.background = '#000000'
   alert("OhYeah!");
   $.ajax({
        url: 'http://127.0.0.1:5000/record/',
        method: 'POST',
        success: function(data) {
            alert(data['speech']);
        }
   })
}
