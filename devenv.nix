{
  pkgs,
  lib,
  config,
  ...
}: {
  packages = with pkgs; [
    python313Packages.numpy
  ];
  languages.python.enable = true;
  languages.python.venv.enable = true;
  languages.python.venv.requirements = ''
    pandas
    seaborn
    matplotlib
    jupyter
  '';

  # See full reference at https://devenv.sh/reference/options/
}
