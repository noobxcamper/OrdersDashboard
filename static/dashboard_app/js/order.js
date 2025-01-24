var modalDialog = $('#modal-dialog');
var modalOpen = $('#modal-open');
var modalClose = $('#modal-close');
var back = $('#back-btn');
var completeOrder = $('#complete-order-btn');
var closeOrder = $('#close-order-btn');
var updateOrder = $('#update-order-btn');
var saveNotes = $('#save-notes-btn');
var notesField = $('#private-notes');
var trackingUrlField = $('#tracking-url-field');

modalOpen.click(function () {
    modalDialog.removeClass('modal-closed');
});

modalClose.click(function () {
    modalDialog.addClass('modal-closed');
});

completeOrder.click(function () {
    if (confirm("Are you sure you want to complete this order?")) {
        // update the order
        $.ajax({
            url: "/api/orders/update/" + $(this).data("order-id"),
            type: "PUT",
            contentType: 'application/json',
            data: JSON.stringify({ "status": "completed" }),
            success: function () {
                window.location.reload();
            }
        });
    }
});

closeOrder.click(function () {
    if (confirm("Are you sure you want to close this order?")) {
        // update the order
        $.ajax({
            url: "/api/orders/update/" + $(this).data("order-id"),
            type: "PUT",
            contentType: 'application/json',
            data: JSON.stringify({ "status": "closed" }),
            success: function () {
                window.location.reload();
            }
        });
    }
});

updateOrder.click(function () {
    if (confirm("Are you sure you want to update the tracking URL for this order?")) {
        // update the order
        $.ajax({
            url: "/api/orders/update/" + $(this).data("order-id"),
            type: "PUT",
            contentType: 'application/json',
            data: JSON.stringify({ "tracking_url": trackingUrlField.val() }),
            success: function () {
                window.location.reload();
            }
        });
    }
});

saveNotes.click(function () {
    // update the order
    $.ajax({
        url: "/api/orders/update/" + $(this).data("order-id"),
        type: "PUT",
        contentType: 'application/json',
        data: JSON.stringify({ "private_notes": notesField.val() }),
        success: function() {
            alert("Notes saved!");
        }
    });
});

back.click(function () {
    window.location.href = '/';
});