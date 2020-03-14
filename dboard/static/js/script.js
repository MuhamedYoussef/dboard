(function() {
    var img = new Image,
        url = encodeURIComponent(document.location.href),
        title = encodeURIComponent(document.title),
        ref = encodeURIComponent(document.referrer);
    img.src = `DOMAIN/analytics/analyse?url=${url}&title=${title}&ref=${ref}`;
})();