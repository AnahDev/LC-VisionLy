const fs = require('fs');

function parseDockerNetwork(filePath) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n');
    
    let networksCount = 0;
    let subnetsCount = 0;

    lines.forEach(line => {
        const lineStr = line.trim();
        if (lineStr.includes('net_interface_')) {
            networksCount++;
        }
        if (lineStr.startsWith('subnet:')) {
            subnetsCount++;
        }
    });

    return { networksCount, subnetsCount };
}

const args = process.argv.slice(2);
if (args.length > 0) {
    parseDockerNetwork(args[0]);
}