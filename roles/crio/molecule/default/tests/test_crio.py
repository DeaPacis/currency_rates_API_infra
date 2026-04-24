import pytest

def test_crio_package_installed(host):
    pkg = host.package("cri-o")
    assert pkg.is_installed


def test_crio_service_running(host):
    service = host.service("crio")
    assert service.is_enabled
    assert service.is_running


def test_crio_config_file(host):
    file = host.file("/etc/crio/crio.conf.d/20-cgroup-driver.conf")
    assert file.exists
    assert file.contains("cgroup_manager")


@pytest.mark.parametrize("pkg", [
    "conmon",
    "containernetworking-plugins",
])
def test_crio_dependencies(host, pkg):
    assert host.package(pkg).is_installed


def test_crio_version(host):
    cmd = host.run("crio --version")
    assert cmd.rc == 0


def test_crio_service_exists(host):
    svc = host.service("crio")
    assert svc.exists
