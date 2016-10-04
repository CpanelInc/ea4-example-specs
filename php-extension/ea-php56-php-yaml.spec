Name: ea-php56-php-yaml
Version: 1.2.0
Summary: YAML PECL extension for PHP 5.6
Release: 1%{?dist}
License: MIT
Group: Programming/Languages
URL: http://bd808.com/pecl-file_formats-yaml/
Source: https://pecl.php.net/get/yaml-1.2.0.tgz
Source1: yaml.ini

Requires: libyaml
BuildRequires: libyaml-devel
BuildRequires: ea-php56 ea-php56-php-cli

%description
Support for YAML 1.1 (YAML Ain't Markup Language) serialization using the LibYAML library.

%prep
%setup -n yaml-%{version}

%build
scl enable ea-php56 phpize
scl enable ea-php56 ./configure
make

%install
scl enable ea-php56 'make install INSTALL_ROOT=%{buildroot}'
install -m 755 -d $RPM_BUILD_ROOT/opt/cpanel/ea-php56/root/etc/php.d/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/opt/cpanel/ea-php56/root/etc/php.d/

%clean
%{__rm} -rf %{buildroot}

%files
/opt/cpanel/ea-php56/root/%{_libdir}php/modules/yaml.so
/opt/cpanel/ea-php56/root/etc/php.d/yaml.ini

%changelog
* Thu Sep 15 2016 Matt Dees <matt@cpanel.net> - 1.2.0-1
- Initial spec file creation.
