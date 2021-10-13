function select_category(value)
 {
     console.log($("#category").prop('value'))
     $("#category").prop('value', value)
 }

function home()
    {
        $.ajax({
            url: "{% url list_recruitments %}",
            method: "get",
            
        })
    }