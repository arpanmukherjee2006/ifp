const fs = require('fs');
let html = fs.readFileSync('components/footer.html', 'utf8');

// Replace > with >\n to make it easier to read
html = html.replace(/></g, '>\n<');
fs.writeFileSync('components/footer.html', html);
