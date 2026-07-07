function transform(input) {
    var obj = JSON.parse(input);
    if (obj.order_status === 'Delivered') {
        return JSON.stringify(obj);
    }
    return null;
}