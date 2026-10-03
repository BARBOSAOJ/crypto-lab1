// A.13
var zlib = require('zlib');

var inputs = ["eJzzyc9Lyc8DAAgpAms=", "eJxzSi3KycwDAAfXAl0=", "eJzzSy1XiMwvygYADKUC8A=="];
inputs.forEach(function (s) {
    console.log(s + " -> " + zlib.inflateSync(Buffer.from(s, 'base64')).toString());
});

function randomText(n) {
    var chars = "abcdefghijklmnopqrstuvwxyz", out = "";
    for (var i = 0; i < n; i++) out += chars[Math.floor(Math.random() * chars.length)];
    return out;
}
console.log("\nlength | 'abc' repeated -> compressed | random -> compressed");
[3, 30, 300, 3000].forEach(function (n) {
    var rep = "abc".repeat(n / 3), rnd = randomText(n);
    var c1 = zlib.deflateSync(rep).toString('base64'), c2 = zlib.deflateSync(rnd).toString('base64');
    console.log(n + " | " + c1.length + " | " + c2.length);
});
