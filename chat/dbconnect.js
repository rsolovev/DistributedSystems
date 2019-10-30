const mongoose = require("mongoose");
mongoose.Promise = require("bluebird");

const url = "mongodb://localhost:27017,node1:27107,node2:271017,node3:27017/chat";

const connect = mongoose.connect(url, { useNewUrlParser: true });

module.exports = connect;
