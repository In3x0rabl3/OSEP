function paramattributes 
{

    param (
    [Parameter (Mandatory = $True, Position=0, ValueFromPipeline = $True, ParameterSetName="ParamSet1")]
    [ValidateSet(1,2,3)]
#   [AllowNull()]
    $a,

    [Parameter (Mandatory = $True, Position=1)]
    [AllowNull()]
    $b
    )

    Write-Output "a is $a"
    Write-Output "b is $b"

}