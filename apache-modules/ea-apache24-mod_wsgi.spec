Name: ea-apache24-mod_wsgi
Version: 4.5.7
Summary: A WSGI compliant interface for hosting Python based web applications on top of the Apache web server
Release: 2%{?dist}
License: Apache License, Version 2.0
Group: System Environment/Daemons
URL: http://modwsgi.org
Source: https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.7.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ea-apache24-devel
BuildRequires: python-devel
Requires: ea-apache24
Requires: python redhat-rpm-config

%description
A WSGI compliant interface for hosting Python based web applications on top of the Apache web server

%prep
%setup -q

%{__cat} <<EOF > mod_wsgi.conf
### Load the module
LoadModule wsgi_module modules/mod_wsgi.so

EOF


%build
%configure --prefix=%{_sysconfdir}/apache2 --exec-prefix=%{_prefix}
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%make_install
%{__install} -Dp -m0644 mod_wsgi.conf %{buildroot}%{_sysconfdir}/apache2/conf.d/mod_wsgi.conf

%clean
%{__rm} -rf %{buildroot}

%files
%{_libdir}/apache2/modules/mod_wsgi.so
%config(noreplace) %{_sysconfdir}/apache2/conf.d/mod_wsgi.conf

%changelog
* Thu Sep 15 2016 Kenneth Power <kenneth.power@gmail.com> - 4.5.7-2
- Initial spec file creation.
EOF
