%define debug_package %{nil}

%define import_path github.com/russross/blackfriday
%define gopath %{_libdir}/go
%define gosrc %{gopath}/src/%{import_path}

Summary:	Markdown processor for Go
Name:		golang-blackfriday
Version:	2.1.0
Release:	1
License:	BSD
Group:		Development/Other
Url:		https://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
Provides:       golang(%{import_path}) = %{version}-%{release}

%package devel
BuildRequires:  golang >= 1.3.3
BuildRequires:	golang-net-devel
Requires:       golang >= 1.3.3
Summary:        Markdown processor for Go

%description
Blackfriday is a markdown processor for Go

%description devel
Blackfriday is a markdown processor for Go devel part

%prep
%setup -q -n blackfriday-%{version}

%build
go build

%install
mkdir -p %{buildroot}%{gosrc}
for d in . ; do
    install -d -p %{buildroot}/%{gosrc}/$d
    cp -av $d/*.go %{buildroot}/%{gosrc}/$d
done
rm -f %{buildroot}%{gosrc}/{README.md}

%files
%doc README.md

%files devel
%doc README.md
%dir %attr(755,root,root) %{gosrc}
%{gosrc}/*.go
