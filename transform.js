function transform(line) {
    // Split CSV line into an array. Assuming simple CSV without quoted commas.
    var columns = line.split(',');

    var obj = new Object();
    // Assuming the order of columns matches the BigQuery Schema
    obj.order_id = columns[0];
    obj.product = columns[1];
    obj.quantity = columns[2];
    obj.order_status = columns[3];
    obj.order_date = columns[4];

    // Check if order_status is 'Completed'
    if (obj.order_status === 'Completed') {
        // Return a JSON string
        return JSON.stringify(obj);
    }

    // Return null to filter out the record
    return null;
}