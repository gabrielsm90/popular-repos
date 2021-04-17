import mock
from requests import Response

from services.health_check.application import scheduler
from services.health_check.application.api_client import check_popular_repo_app_health


def test_start_scheduler():
    """Test creation of scheduler."""
    assert len(scheduler.get_jobs()) == 1


@mock.patch("logging.info")
@mock.patch("requests.get")
def test_health_check_with_success(mocked_request: mock.MagicMock, mocked_log: mock.MagicMock):
    """Test health check with success."""
    response = Response()
    response.status_code = 200
    mocked_request.return_value = response
    check_popular_repo_app_health()
    mocked_log.assert_called_once_with("Application healthy.")


@mock.patch("logging.error")
@mock.patch("requests.get")
def test_health_check_with_fail(mocked_request: mock.MagicMock, mocked_log: mock.MagicMock):
    """Test health check with success."""
    response = Response()
    response.status_code = 500
    mocked_request.return_value = response
    check_popular_repo_app_health()
    mocked_log.assert_called_once()



