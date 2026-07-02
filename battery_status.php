<?php
header('Content-Type: application/json');

$output = shell_exec('python3 /usr/local/bin/battery_monitor.py 2>&1');
preg_match('/(\d+\.?\d*)V \((\d+)%\)/', $output, $matches);

if ($matches) {
    echo json_encode([
        'voltage' => (float)$matches[1],
        'percentage' => (int)$matches[2],
        'timestamp' => date('Y-m-d H:i:s')
    ]);
} else {
    http_response_code(500);
    echo json_encode(['error' => 'Unable to read UPS']);
}
?>