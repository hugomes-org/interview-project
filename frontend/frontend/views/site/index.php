<?php

/** @var yii\web\View $this */

$this->title = 'My Yii Application';
?>
<div class="site-index">

<h2 class="title">My Data from API</h2>
<h5>Value <?= $myVal ?></h5>
<table class="table">
    <thead>
        <tr>
            <th scope="col">#</th>
        </tr>
    </thead>
    <tbody>
        <?php
        for ($i = 0; $i < count($myDatas); $i++) {
        ?>
            <tr>
                <th scope="row"><?= $myDatas[$i]['value'] ?></th>
            </tr>
        <?php } ?>
    </tbody>
</table>
</div>