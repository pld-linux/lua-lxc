Summary:	Lua binding for LXC
Summary(pl.UTF-8):	Wiązanie Lua do LXC
Name:		lua-lxc
Version:	3.0.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
# Source0-md5:	6c7a25c78d7ffc1589c93e9fcba9a000
URL:		https://linuxcontainers.org/lxc/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	lxc-devel >= 3.0.0
BuildRequires:	pkgconfig
Requires:	lua51-libs >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lua binding for LXC.

%description -l pl.UTF-8
Wiązanie Lua do LXC.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LUA_VERSION=5.1 \
	--with-lua-pc=lua5.1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/lua/*.*/lxc
%attr(755,root,root) %{_libdir}/lua/*.*/lxc/core.so
%{_datadir}/lua/*.*/lxc.lua
