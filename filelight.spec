Summary:	Graphical disk usage statistics
Summary(pl):	Graficzne statystyki zaj�cia dysku
Name:		filelight
Version:	0.6.4
Release:	1
License:	GPL
Vendor:		Max Howell <max.howell@methylblue.com>
Url:		http://www.methylblue.com/filelight

Group:		X11/Applications
Source0:	http://www.methylblue.com/%{name}/%{name}-%{version}-%{release}.tar.gz
# Source0-md5:	363c71fa5125a57aa0252ffa8d65c647
BuildRequires:	kdebase-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)



%define		_htmldir	/usr/share/doc/kde/HTML

%description
Filelight graphically represents a file system as a set of concentric
segmented-rings, indicating where diskspace is being used. Segments
expanding from the center represent files (including directories),
with each segment's size being proportional to the file's size and
directories having child segments. Filelight performs a similar
function to KDirstat, but in a more compact fashion.

%description -l pl
Filelight przedstawia graficznie objeto�� systemu plik�w.

%prep
%setup -q


%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_appsdir="%{_applnkdir}"; export kde_appsdir


%configure \
	--prefix `kde-config --prefix`  \
	--enable-final \
	--disable-debug

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%find_lang %{name} --with-kde


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_applnkdir}/Utilities/%{name}.desktop
%{_datadir}/config/%{name}rc
%{_pixmapsdir}/*/*/apps/%{name}.png
