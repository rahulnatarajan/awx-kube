# awx.main.utils.reload
from awx.main.utils import reload


def test_produce_supervisor_command(mocker):
    communicate_mock = mocker.MagicMock(return_value=('Everything is fine', ''))
    mock_process = mocker.MagicMock()
    mock_process.communicate = communicate_mock
    Popen_mock = mocker.MagicMock(return_value=mock_process)
    with mocker.patch.object(reload.subprocess, 'Popen', Popen_mock):
        reload._supervisor_service_command(['beat', 'callback', 'fact'], "restart")
        reload.subprocess.Popen.assert_called_once_with(
            ['supervisorctl', 'restart', 'tower-processes:receiver',],
            stderr=-1, stdin=-1, stdout=-1)

