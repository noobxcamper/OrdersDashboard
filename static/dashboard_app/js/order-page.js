var modalDialog = $('#modal-dialog');
var modalOpen = $('#modal-open');
var modalClose = $('#modal-close');

modalOpen.click(function () {
    modalDialog.removeClass('modal-closed');
});

modalClose.click(function () {
    modalDialog.addClass('modal-closed');
});

// ('#complete-order-btn').click(function () {
//     if (confirm("Are you sure you want to complete this order?")) {
//         // finish order
//         // send email, teams message or whatever

//         // update the order
//         $.ajax({
//             url: "/api/updateorder/" + $(this).data("order-id"),
//             type: "PUT",
//             contentType: 'application/json',
//             data: JSON.stringify({ "status": "completed" }),
//             success: function () {
//                 window.location.href = '/'
//             }
//         });
//     }
// });

// $('#close-order-btn').click(function () {
//     if (confirm("Are you sure you want to close this order?")) {
//         // finish order
//         // send email, teams message or whatever

//         // update the order
//         $.ajax({
//             url: "/api/updateorder/" + $(this).data("order-id"),
//             type: "PUT",
//             contentType: 'application/json',
//             data: JSON.stringify({ "status": "closed" }),
//             success: function () {
//                 window.location.href = '/'
//             }
//         });
//     }
// });

// $('#private-notes').focusout(function () {
//         $.ajax({
//             url: "/api/updateorder/" + $(this).data("order-id"),
//             type: "PUT",
//             contentType: 'application/json',
//             data: JSON.stringify({"private_notes": $(this).val()})
//         });
// });

$('#back-btn').click(function () {
    window.location.href = '/';
});