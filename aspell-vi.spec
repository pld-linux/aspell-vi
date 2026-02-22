Summary:	Vietnamese dictionary for aspell
Summary(pl.UTF-8):	Słownik wietnamski dla aspella
Name:		aspell-vi
Version:	0.01.1
%define	subv	1
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/vi/aspell6-vi-%{version}-%{subv}.tar.bz2
# Source0-md5:	314185e521900df0fab8375fa609bba2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vietnamese dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik wietnamski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-vi-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
