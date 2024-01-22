Name:        cri-dockerd
Version:     0.3.9
Release:     5c1b469%{?dist}
Summary:     cri-dockerd

License:     Apache-2.0
URL:         https://github.com/iscas-fork/cri-dockerd 
Source0:     %{name}-%{version}.tar.gz

Requires: docker-ce

%description

%prep
%setup -n %{name}-%{version}
cp -r /root/rpmbuild/BUILD/%{name}-%{version} /root/rpmbuild/BUILDROOT/%{name}-%{version}-%{release}.x86_64

%files
%defattr (-,root,root,0755)
/usr/bin/cri-dockerd
/usr/lib/systemd/system/cri-docker.service
/usr/lib/systemd/system/cri-docker.socket
