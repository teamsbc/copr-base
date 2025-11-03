%global dist_version %{fedora}

Name:           teamsbc-repos
Version:        %{dist_version}
Release:        1
Summary:        Fedora TeamSBC Remix package repositories

License:        MIT

Provides:       teamsbc-repos(%{version}) = %{release}
Requires:       system-release(%{version})

BuildArch:      noarch

Source1:        teamsbc-base.repo

%description
Fedora package repository files for yum and dnf.

%prep

%build

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -m 644 %{_sourcedir}/teamsbc*repo %{buildroot}%{_sysconfdir}/yum.repos.d

%check

%files
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/teamsbc-base.repo

%changelog
* Mon Nov 03 2025 Simon de Vlieger <cmdr@supakeen.com> - %{fedora}-1
- Initial setup of Fedora TeamSBC Remix's package repositories package.
