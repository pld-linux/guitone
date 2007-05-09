Summary:	A GUI frontend for monotone
Summary(pl.UTF-8):	Graficzny interfejs użytkownika dla monotone
Name:		guitone
Version:	0.6.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://guitone.thomaskeller.biz/count.php/from=default/%{version}/%{name}-%{version}.tgz
# Source0-md5:	c57e23e156d36b32db4ffe87614ddde9
URL:		http://guitone.thomaskeller.biz/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build >= 4.2.0
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	monotone >= 0.34
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guitone is a Qt-based, cross-platform graphical user interface for the
distributed version control system monotone. It aims towards a full
implementation of the monotone automation interface and is especially
targeted at beginners.

%description -l pl.UTF-8
Guitone to oparty na Qt, wieloplatformowy graficzny interfejs
użytkownika do rozproszonego systemu kontroli wersji monotone. Jego
celem jest pełna implementacja interfejsu automatyzacji monotona i
jest przeznaczony zwłaszcza dla początkujących.

%prep
%setup -q

%build
qt4-qmake -config release guitone.pro
%{_libdir}/qt4/bin/lrelease guitone.pro

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc notes/* NEWS README
%attr(755,root,root) %{_bindir}/*
