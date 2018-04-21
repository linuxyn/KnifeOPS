/**
 * Created by Administrator on 2018/4/21.
 */
$(function () {
    // DataTables响应式
    $(document).ready(function() {
        var table = $('#example1').DataTable( {
        "scrollY": "370px",
        "paging": true
    } );

    $('a.toggle-vis').on( 'click', function (e) {
        e.preventDefault();

        // Get the column API object
        var column = table.column( $(this).attr('data-column') );

        // Toggle the visibility
        column.visible( ! column.visible() );
        } );
    } );

   $("table").find('tr').each(function () {
       console.log("start log");
       var content = $(this).find("td").eq(4).text();
       $(this).find("td").eq(4).text("");
       var label_tag = "";
       if(content=="A"){
           label_tag = "label-success";
           $(this).find("td").eq(4).append('<span></span>').addClass("label").addClass(label_tag).text(content);
       console.log("content-->", content)}
       else if(content=="C"){
           label_tag = "label-danger";
           $(this).find("td").eq(4).append('<span></span>').addClass("label").addClass(label_tag).text(content);
       }
       else if(content=="X"){
           label_tag = "label-info";
           $(this).find("td").eq(4).append('<span></span>').addClass("label").addClass(label_tag).text(content);
       }
       else {
           label_tag = "label-warning";
           $(this).find("td").eq(4).append('<span></span>').addClass("label").addClass(label_tag).text(content);
       }
   });
})
